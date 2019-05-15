from django.core.management.base import BaseCommand
# from django.utils import timezone
import os
from os.path import dirname
import json

from bs4 import BeautifulSoup as BS
from os.path import basename, splitext



def process_image_file(question_html = ''):
    base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
    soup = BS(question_html,features='html.parser')
    for img in soup.findAll('img'):
        img['src'] = base_dir + splitext(basename(img['src']))[0]
    question_html = str(soup)
    print(question_html)

process_image_file('''"questionHtml": "Complete the following multiplication table:<br \/>\r\n<img alt=\"\" src=\"img\/4_Q.png\" style=\"width: 424px; height: 234px;\" \/><br \/>\r\nIs the multiplication table symmetrical about the diagonal joining the upper left corner to the lower right corner?",''')