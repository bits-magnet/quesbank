from django.core.management.base import BaseCommand
import os
from os.path import dirname
import json
from api.models import *
from .services.predictLevel import predictLevel
from .services.findLength import findLength
from .services.findOptions import findOptions
from .services.categorize_questions import categorize

class Command(BaseCommand):
    help = ''' to transform all the json data to classify questions to Subjective/Objective,
     Short/Long/VeryLong and predict level of problem'''

    def handle(self, *args, **kwargs):
        base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
        directory = base_dir + '/books/'
        for standard in os.listdir(directory):
            for subject in os.listdir(directory + '/' + standard):
                for book in os.listdir(directory + '/' + standard + '/' + subject):
                    print(book)
                    for topic in os.listdir(directory + '/' + standard + '/' + subject + '/' + book + '/' + 'html' + '/'):
                        topic_id, topic_name = topic.split('_', 1)
                        for files in os.walk(directory + '/' + standard + '/' + subject + '/' + book + '/' + 'html' + '/' + topic + '/'):
                            for file in files[2]:
                                if '.json' in file:
                                    flag = True
                                    with open(
                                            base_dir + '/books' + '/' + standard + '/' + subject + '/' + book + '/html' + '/' + topic + '/' + file,
                                            'r') as f:
                                        data = json.load(f)
                                        dictionary = predictLevel(data['data'])
                                        text_id = None
                                        if flag:
                                            for x in data['data']:
                                                text_id = x['textbookId']
                                                chapter_id = x['chapterId']
                                                flag = False

                                        for question_id in dictionary:
                                            inquestion = InQuestion.objects.get(question_id = question_id, text_book_id = text_id, chapter_id = chapter_id)
                                            if inquestion:
                                                inquestion.question_level = dictionary[question_id]
                                                question = Question.objects.filter(inquestion = inquestion)
                                                for ques in question:
                                                    ques.level = dictionary[question_id]
                                                    ques.save()
                                                # except:
                                                #     print('Error: Ambiguity in question')
                                                inquestion.save()

        print('*'*50, 'completed predicting level for questions', '*'*50)
        print('*'*50, 'Categorising questions into level of difficulties', '*'*50)
        questions = InQuestion.objects.all()
        for question in questions:
            question_type = str(categorize(question.question_html, question.solution_html, question.exercise_name))
            length = findLength(question.solution_html)
            if question_type == 'Subjective':
                subjective_question, updated = SubjectiveQuestion.objects.get_or_create(question_type = 'Subjective', length = length, inquestion = question, topic = question.topic, state = 'imported')
                subjective_question.question_html = question.question_html
                subjective_question.solution_html = question.solution_html
                subjective_question.save()
            elif question_type == 'Objective':
                objective_question, updated = ObjectiveQuestion.objects.get_or_create(question_type = 'Objective', length = length, inquestion = question, topic = question.topic, state = 'imported')
                objective_question.question_html = question.question_html
                objective_question.solution_html = question.solution_html
                result = findOptions(objective_question.question_html, objective_question.solution_html)
                if result['options']:
                    objective_question.options = result['options']
                else:
                    objective_question.options = ['no option']
                try:
                    if result['correct']:
                        objective_question.correct_option = result['correct']
                    else:
                        objective_question.correct_option = ['no answer']
                except Exception as e:
                    print('ERROR OCCOURED ->', e, '*'*50)
                objective_question.save()
        print('*'*50,'All Question categorised','*'*50)
