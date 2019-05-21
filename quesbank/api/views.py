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
from .services import *


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
    filter_fields = ('topic','state')
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


def subjective(request):
    return render(request, 'subjective.html')


def objective(request):
    return render(request, 'objective.html')


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SubjectiveQuestion


class SubjectiveQuestionCreate(CreateView):
    model = SubjectiveQuestion
    fields = '__all__'


class SubjectiveQuestionUpdate(UpdateView):
    model = SubjectiveQuestion
    fields = '__all__'


class SubjectiveQuestionDelete(DeleteView):
    model = SubjectiveQuestion
    success_url = reverse_lazy('subjective_question')


class ObjectiveQuestionCreate(CreateView):
    model = ObjectiveQuestion
    fields = '__all__'


class ObjectiveQuestionUpdate(UpdateView):
    model = ObjectiveQuestion
    fields = '__all__'


class ObjectiveQuestionDelete(DeleteView):
    model = ObjectiveQuestion
    success_url = reverse_lazy('subjective_question')


def success(request):
    return render(request, 'success.html')


#######################  subjective question views ###########################################

def subjective_duplicates(request, subjective_question_id):
    subjective_question = SubjectiveQuestion.objects.get(pk=subjective_question_id)
    if not subjective_question.state == 'duplicate':
        return render(request, 'no_duplicates.html')
    similar_questions = SimilarSubjectiveQuestion.objects.filter(question = subjective_question.id, similar_to_question__state = 'duplicate')

    context = {
        'subjective_question' : subjective_question,
        'similar_questions': similar_questions
    }
    print(context['similar_questions'])
    return render(request, 'subjective_duplicate.html', context=context)


def subjective_archieve(request, subjective_question_id):
    subjective_question = SubjectiveQuestion.objects.get(pk = subjective_question_id)
    archieve_subjective_question = ArchievedSubjectiveQuestion.objects.create(inquestion = subjective_question.inquestion,
                                                                              question_html = subjective_question.inquestion.question_html,
                                                                              solution_html = subjective_question.inquestion.solution_html,
                                                                              question_type = subjective_question.question_type,
                                                                              updated_at = subjective_question.updated_at,
                                                                              topic = subjective_question.topic,
                                                                              state = 'rejected',
                                                                              level = subjective_question.level,
                                                                              length = subjective_question.length
                                                                              )

    similar_subjective_questions = SimilarSubjectiveQuestion.objects.filter(similar_to_question = subjective_question)

    for similar_subjective_question in similar_subjective_questions:
        similar_subjective_question.delete()
    subjective_question.delete()
    archieve_subjective_question.save()
    print(archieve_subjective_question)
    return render(request, 'success.html')

def subjective_approve(request, subjective_question_id):
    subjective_question = SubjectiveQuestion.objects.get(pk=subjective_question_id)
    subjective_question.state = 'approved'
    subjective_question.save()
    return render(request, 'success.html')


#######################  objective question views ###########################################

def objective_duplicates(request, objective_question_id):
    objective_question = SubjectiveQuestion.objects.get(pk=objective_question_id)
    if not objective_question.state == 'duplicate':
        return render(request, 'no_duplicates.html')
    similar_questions = SimilarSubjectiveQuestion.objects.filter(question = objective_question.id, similar_to_question__state = 'duplicate')

    context = {
        'objective_question' : objective_question,
        'similar_questions': similar_questions
    }
    print(context['similar_questions'])
    return render(request, 'objective_duplicate.html', context=context)


def objective_archieve(request, objective_question_id):
    objective_question = ObjectiveQuestion.objects.get(pk = objective_question_id)
    archieve_objective_question = ArchievedObjectiveQuestion.objects.create(inquestion = objective_question.inquestion,
                                                                              question_html = objective_question.inquestion.question_html,
                                                                              solution_html = objective_question.inquestion.solution_html,
                                                                              question_type = objective_question.question_type,
                                                                              options = objective_question.options,
                                                                              correct_option = objective_question.correct_option,
                                                                              updated_at = objective_question.updated_at,
                                                                              topic = objective_question.topic,
                                                                              state = 'rejected',
                                                                              level = objective_question.level,
                                                                              length = objective_question.length
                                                                              )

    similar_objective_questions = SimilarObjectiveQuestion.objects.filter(similar_to_question = objective_question)

    for similar_objective_question in similar_objective_questions:
        similar_objective_question.delete()
    objective_question.delete()
    archieve_objective_question.save()
    print(archieve_objective_question)
    return render(request, 'success.html')


def objective_approve(request, objective_question_id):
    objective_question = ObjectiveQuestion.objects.get(pk=objective_question_id)
    objective_question.state = 'approved'
    objective_question.save()
    return render(request, 'success.html')
