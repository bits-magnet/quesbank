from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter
from rest_framework import generics
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status,filters
import django_filters
from django.template import Template
from rest_framework.permissions import IsAuthenticated

class StandardList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StandardSerializer
    queryset = Standard.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class StandardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer


class SubjectList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TopicList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class SubjectiveQuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubjectiveQuestionSerializer
    queryset = SubjectiveQuestion.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class SubjectiveQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SubjectiveQuestion.objects.all()
    serializer_class = SubjectiveQuestionSerializer


class ObjectiveQuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ObjectiveQuestionSerializer
    queryset = ObjectiveQuestion.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class ObjectiveQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ObjectiveQuestion.objects.all()
    serializer_class = ObjectiveQuestionSerializer


class SimilarSubjectiveQuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SimilarSubjectiveQuestionSerializer
    queryset = SimilarSubjectiveQuestion.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class SimilarSubjectiveQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SimilarSubjectiveQuestion.objects.all()
    serializer_class = SimilarSubjectiveQuestionSerializer


class SimilarObjectiveQuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SimilarObjectiveQuestionSerializer
    queryset = SimilarObjectiveQuestion.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = '__all__'
    ordering_fields = '__all__'


class SimilarObjectiveQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SimilarObjectiveQuestion.objects.all()
    serializer_class = SimilarObjectiveQuestionSerializer


def ques_bank(request):
    return render(request,'main.htm')

def subject(request,pk):
    return render(request, 'subject.html',{'subjectId':pk})

def topic(request,sub_key,topic_key):
    return render(request, 'topic.html', {'subjectId':sub_key, 'topicId' : topic_key})


def ckeditor(request):
    question = InQuestion.objects.filter(topic = 10)
    context = {'questions': question}
    return render(request, 'ckeditor_template.html', context)