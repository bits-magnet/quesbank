from django.core.management.base import BaseCommand
# from django.utils import timezone
import os
from os.path import dirname
import json
from api.models import *
from api.serializers import *
from bs4 import BeautifulSoup as BS
from os.path import basename, splitext


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

# def process_image_file(question_html = ''):
#     base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
#     soup = BS(question_html,features='html.parser')
#     for img in soup.findAll('img'):
#         img['src'] = base_dir + splitext(basename(img['src']))[0]
#     question_html = str(soup)
#     print(question_html)
#     print(base_dir)
#
# process_image_file('''"questionHtml": "Complete the following multiplication table:<br \/>\r\n<img alt=\"\" src=\"img\/4_Q.png\" style=\"width: 424px; height: 234px;\" \/><br \/>\r\nIs the multiplication table symmetrical about the diagonal joining the upper left corner to the lower right corner?",''')

