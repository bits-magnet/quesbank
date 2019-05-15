from django.core.management.base import BaseCommand
import os
from os.path import dirname
import json
from api.models import *


class Command(BaseCommand):
    help = ''' to transform all the json data to classify questions to Subjective/Objective,
     Short/Long/VeryLong and predict level of problem'''

    def handle(self, *args, **kwargs):
        pass

