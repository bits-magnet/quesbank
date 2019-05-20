from django.core.management.base import BaseCommand
import json
from api.models import *
from api.serializers import *


class Command(BaseCommand):
    help = ''' to transform all the json data to classify questions to Subjective/Objective,
     Short/Long/VeryLong and predict level of problem'''

    def handle(self, *args, **kwargs):
        data = {}
        data['data'] = []
        for subj in SubjectiveQuestion.objects.filter(question__topic__topic='Integers'):
            data['data'].append({
                'id': subj.id,
                'question_html' : subj.question_html,
                'solution_html' : subj.solution_html
            })
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
