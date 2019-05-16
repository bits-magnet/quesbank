from django.core.management.base import BaseCommand
import os
from os.path import dirname
import json
from api.models import *
from .predictLevel import predictLevel
from .findLength import findLength
from .findOptions import findOptions
from .categorize_questions import categorize

class Command(BaseCommand):
    help = ''' to transform all the json data to classify questions to Subjective/Objective,
     Short/Long/VeryLong and predict level of problem'''

    def handle(self, *args, **kwargs):
        base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
        directory = base_dir + '/books/'
        for standard in os.listdir(directory):
            for subject in os.listdir(directory + '/' + standard):
                for book in os.listdir(directory + '/' + standard + '/' + subject):
                    for topic in os.listdir(directory + '/' + standard + '/' + subject + '/' + book + '/' + 'html' + '/'):
                        topic_id, topic_name = topic.split('_', 1)
                        for file in os.walk(directory + '/' + standard + '/' + subject + '/' + book + '/' + 'html' + '/' + topic + '/'):
                            if '.json' in file:
                                with open(
                                        base_dir + '/books' + '/' + standard + '/' + subject + '/' + book + '/html' + '/' + topics + '/' + file,
                                        'r') as f:
                                    data = json.load(f)
                                    dictionary = predictLevel(data['data'])
                                    for question_id, level in dictionary:
                                        inquestion = InQuestion.objects.get(question_id = question_id)
                                        if(len(inquestion)==1):
                                            inquestion.question_level = level
                                            inquestion.save()
        print('completed predicting level for questions')
        questions = InQuestion.objects.all()
        for question in questions:
            # ques, updated  = Question.objects.get_or_create(inquestion = question, level = question.question_level, topic = question.topic)
            question_type = str(categorize(question.question_html, question.solution_html, question.exercise_name))
            length = findLength(question.solution_html)
            if(question_type == 'Subjective'):
                subjective_question, updated = SubjectiveQuestion.objects.get_or_create(question_type = 'Subjective', length = length, inquestion = question, topic = question.topic)
                subjective_question.question_html = question.question_html
                subjective_question.solution_html = question.solution_html
                subjective_question.save()
            elif(question_type == 'Objective'):
                objective_question, updated = ObjectiveQuestion.objects.get_or_create(question_type = 'Objective', length = length, inquestion = question, topic = question.topic)
                objective_question.question_html = question.question_html
                objective_question.solution_html = question.solution_html
                result = findOptions(objective_question.question_html, objective_question.solution_html)
                if(result['options'] != None):
                    objective_question.options = result['options']
                else:
                    objective_question.options = ['no option']
                try:
                    if(result['correct'] != None):
                        objective_question.correct_option = result['correct']
                    else:
                        # print(ques.id, objective_question.question_html, '*' * 100)
                        objective_question.correct_option = ['no answer']
                except Exception as e:
                    print('ERROR OCCOURED ->', e, '*'*50)
                objective_question.save()
        print(str(questions[0]) + 'Question categorised')
