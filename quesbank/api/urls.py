from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('api/standard/', StandardList.as_view()),
    path('api/standard/<int:pk>', StandardDetail.as_view()),
    path('api/subject/', SubjectList.as_view()),
    path('api/subject/<int:pk>', SubjectDetail.as_view()),
    path('api/topic/', TopicList.as_view()),
    path('api/topic/<int:pk>', TopicDetail.as_view()),
    path('api/subjective-question/', SubjectiveQuestionList.as_view()),
    path('api/subjective-question/<int:pk>', SubjectiveQuestionDetail.as_view()),
    path('api/similar-subjective-question/', SimilarSubjectiveQuestionList.as_view()),
    path('api/similar-subjective-question/<int:pk>', SimilarSubjectiveQuestionDetail.as_view()),
    path('api/similar-objective-question/', SimilarObjectiveQuestionList.as_view()),
    path('api/similar-objective-question/<int:pk>', SimilarObjectiveQuestionDetail.as_view()),
    path('question-bank/', ques_bank),
    path('subject/<int:pk>', subject),
    path('subject/<int:sub_key>/topic/<int:topic_key>',topic),
    path('ckeditor', ckeditor)
]
