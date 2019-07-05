import os
from django.http import HttpResponse
from django.core import serializers
from .models import *
# import requests
# from retrying import Retry
# from requests.adapters import HTTPAdapter
#
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
# def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
#     '''
#     provides request object with retry functionality
#     '''
#     session = session or requests.Session()
#     retry = Retry(
#         total=retries,
#         read=retries,
#         connect=retries,
#         backoff_factor=backoff_factor,
#         status_forcelist=status_forcelist,
#     )
#     adapter = HTTPAdapter(max_retries=retry)
#     session.mount('http://', adapter)
#     session.mount('https://', adapter)
#     return session
#
# def upload_media(to_loc,from_loc,replace_old=True):
#     # logger.info(f'uploading media from {from_loc} to {to_loc} with replace as {replace_old}')
#     with open(from_loc,'rb') as from_file:
#         if default_storage.exists(to_loc):
#             # logger.warning("Found same media file at {}".format(to_loc))
#             if replace_old:
#                 # logger.warning("Removing old".format(to_loc))
#                 default_storage.delete(to_loc)
#             return to_loc
#         file_content = ContentFile(from_file.read())
#         return default_storage.save(to_loc,file_content)
#
#
# def download_media(from_url,to_loc,**kwargs):
#     # logger.info(f'downloading {from_url} to location {to_loc}')
#     resp = requests_retry_session().get(from_url)
#     if resp.status_code != 200:
#         raise UnableToDownloadMedia("Unable to download media status code {} url {}".format(resp.status_code,from_url))
#     dir_loc = '/'.join(to_loc.split('/')[:-1])
#     if not os.path.exists(dir_loc):
#         os.makedirs(dir_loc)
#     with open(to_loc, 'wb') as f:
#         f.write(resp.content)
#     return to_loc
#
