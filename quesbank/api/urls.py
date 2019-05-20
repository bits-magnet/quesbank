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
    path('api/objective-question/', ObjectiveQuestionList.as_view()),
    path('api/objective-question/<int:pk>', ObjectiveQuestionDetail.as_view()),
    path('api/similar-subjective-question/', SimilarSubjectiveQuestionList.as_view()),
    path('api/similar-subjective-question/<int:pk>', SimilarSubjectiveQuestionDetail.as_view()),
    path('api/similar-objective-question/', SimilarObjectiveQuestionList.as_view()),
    path('api/similar-objective-question/<int:pk>', SimilarObjectiveQuestionDetail.as_view()),
    path('', ques_bank),
    path('subject/<int:pk>', subject),
    path('subject/<int:sub_key>/topic/<int:topic_key>', topic),
    path('subjective-question/',subjective),
    path('subjective-question/duplicates/<int:subjective_question_id>', subjective_duplicates, name = 'subjective_question_duplicates'),
    path('objective-question/',objective),
    path('success', success, name = 'success'),
    path('subjective-question/archieve/<int:subjective_question_id>',subjective_archieve , name = 'subjective_question_archieve'),
    path('subjective-question/approve/<int:subjective_question_id>', subjective_approve, name='subjective_question_approve'),
    path('subjective-question/question/create', SubjectiveQuestionCreate.as_view(success_url="/success"), name='subjective_question_create' ),
    path('subjective-question/question/<int:pk>', SubjectiveQuestionUpdate.as_view(success_url="/success"), name='subjective_question_update'),
    path('objective-question/question/create', ObjectiveQuestionCreate.as_view(success_url="/success"),name='objective_question_create'),
    path('objective-question/question/<int:pk>', ObjectiveQuestionUpdate.as_view(success_url="/success"),name='objective_question_update'),

]
