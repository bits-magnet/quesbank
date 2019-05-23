import os
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.core import serializers
from .models import *


def download_objective_json(request):
    filename = 'objective_question.json'
    with open("objective_question.json", "w") as out:
        data2 = serializers.serialize("json", ObjectiveQuestion.objects.all())
        out.write(data2)

    with open(filename, 'rb') as f:
        response = HttpResponse(f.read(),content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=%s' % 'whatever_name_will_appear_in_download.json'
        response['Content-Type'] = 'application/json'
        return response
    #
    # # content = FileWrapper(filename)
    # content = file.read()
    # print(content)
    # response = HttpResponse(content, content_type='application/pdf')
    # response['Content-Length'] = os.stat("E:\projects\qls\quesbank\quesbank\\requirements.txt").st_size #os.path.getsize(filename)
    # print(response['Content-Length'])
    # response['Content-Disposition'] = 'attachment; filename=%s' % 'whatever_name_will_appear_in_download.pdf'
    # return response
