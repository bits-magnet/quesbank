from django.core.management.base import BaseCommand
import os
from os.path import dirname
from api.models import *
from .services.getSimilarity import get_sim_matrix


class Command(BaseCommand):
    help = ''' Make sure you have run all the migrations to the database.
           this command will look for all the json files inside books folder present in root directory'''

    def handle(self, *args, **kwargs):
        base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
        topics = Topic.objects.all()
        for topic in topics:
            data = {}
            data['data'] = []
            for subj in SubjectiveQuestion.objects.filter(topic=topic):
                data['data'].append({
                    'id': subj.id,
                    'question_html' : subj.question_html,
                    'solution_html' : subj.solution_html
                })
            result = get_sim_matrix(data)
            for element in result:
                similar_questions_list = element[1]
                question = SubjectiveQuestion.objects.get(pk=element[0])
                print(element[0], element[1])
                for similar_question in similar_questions_list:
                    similar_subjective_question_found = SubjectiveQuestion.objects.get(pk = similar_question[0])
                    if not question.id == similar_subjective_question_found.id:
                        similar_subjective_question_found.state = 'duplicate'
                        similar_subjective_question_found.save()
                        similar_subjective_question, created = SimilarSubjectiveQuestion.objects.get_or_create(question = question,
                                                                                                                       similar_to_question = similar_subjective_question_found,
                                                                                                                        similarity_percentage = similar_question[1])
                        similar_subjective_question.save()
        print('Subjective Question similarity check done according to topics')
        for topic in topics:
            data = {}
            data['data'] = []
            for obje in ObjectiveQuestion.objects.filter(topic=topic):
                data['data'].append({
                    'id': obje.id,
                    'question_html' : obje.question_html,
                    'solution_html' : obje.solution_html
                })
            result = get_sim_matrix(data)
            for element in result:
                question = ObjectiveQuestion.objects.get(pk = element[0])
                similar_questions_list = element[1]
                for similar_question in similar_questions_list:
                    similar_objective_question_found = ObjectiveQuestion.objects.get(pk=similar_question[0])
                    if not question.id == similar_objective_question_found.id:
                        similar_objective_question_found.state = 'duplicate'
                        similar_objective_question_found.save()
                        similar_objective_question, created = SimilarObjectiveQuestion.objects.get_or_create(question=question,
                                                                                                                 similar_to_question = similar_objective_question_found,
                                                                                                                 similarity_percentage=similar_question[1])
                        similar_objective_question.save()
        print('Objective Question similarity check done according to topics')
        print('All the duplicate questions contain DUPLICATE state')
        questions = Question.objects.all()
        for question in questions:
            if(question.state != 'duplicate'):
                question.state = 'processed'
                question.save()
        print('All the non duplicate questions contain PROCESSED state')
