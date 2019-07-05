from django.core.management.base import BaseCommand
from api.models import Topic, InQuestion, SubjectiveQuestion, ObjectiveQuestion
import json
import os
import shutil
from os.path import dirname
from bs4 import BeautifulSoup as BS
from shutil import copy2


def copy_media_file_of_html(html_text):
    base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
    soup = BS(html_text, features='html.parser')
    for img in soup.findAll('img'):
        img['src'] = img['src'].replace('/', '\\')
        try:
            os.makedirs(base_dir + '\\output' + '\\'.join(img['src'].split('\\')[:-1]), exist_ok=True)
            copy2(base_dir + '\\quesbank' + img['src'], base_dir + '\\output' + img['src'])
        except:
            print(base_dir + '\\quesbank' + img['src'] + '\n file not found ***')
    converted_html = str(soup)
    return converted_html


class Command(BaseCommand):
    help = ''' Make sure you have run all the migrations to the database.
           this command will look for all the json files inside books folder present in root directory'''

    def add_arguments(self, parser):
        parser.add_argument('-s', '--std', type=int, help='Enter standard in integer type')
        parser.add_argument('-t', '--topic', type=str, help='input a topic name')
        parser.add_argument('-ver', '--serializer_version', type=str, help='input the version number')
        parser.add_argument('-n', '--filename', type=str, help='Enter the file name. Example : S-CB-E-0606-SC-SC-LSR-X-XX-X-O.data ', )

    def handle(self, *args, **kwargs):
        std = kwargs['std']
        topic_name = kwargs['topic']
        file_name = kwargs['filename']
        version = kwargs['serializer_version']
        if not version:
            version = 1
        base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
        topics = Topic.objects.filter(topic__icontains=topic_name, subject__standard__standard=std)
        n = 1
        if len(topics) > 1:
            for idx, topic in enumerate(topics):
                print(idx+1, ': ', topic.topic)
            print("***please enter the topic number you want to select***")
            n = int(input())
        if not file_name:
            file_name = topics[0].topic
        print('Enter choice \n 1: subjective questions \n 2: objective questions')
        choice = int(input())
        data = {}
        data['data'] = []
        if choice == 1:
            for subj in SubjectiveQuestion.objects.filter(topic=topics[n-1]):
                question_html = copy_media_file_of_html(subj.question_html)
                solution_html = copy_media_file_of_html(subj.solution_html)
                data['data'].append({
                    'version': version,
                    'question_text': question_html,
                    'solution_text': solution_html,
                    'length': subj.length,
                    'level_order': subj.level
                })
            with open('output\\' + file_name + '.json', 'w') as outfile:
                json.dump(data['data'], outfile)
            shutil.make_archive(file_name, 'zip', 'output')
        else:
            for obj in ObjectiveQuestion.objects.filter(topic=topics[n-1]):
                question_html = copy_media_file_of_html(obj.question_html)
                solution_html = copy_media_file_of_html(obj.solution_html)
                data['data'].append({
                    'version': version,
                    'objective_question_type': 'single',
                    'question_text': question_html,
                    'solution_text': solution_html,
                    'option': obj.options,
                    'correct_option': obj.correct_option,
                    'length': obj.length,
                    'level_order': obj.level
                })
            with open('output\\' + file_name + '.json', 'w') as outfile:
                json.dump(data['data'], outfile)
            shutil.make_archive(file_name, 'zip', 'output')
        shutil.rmtree('output', ignore_errors=False, onerror=None)
        print(file_name, 'zip created at', base_dir)
