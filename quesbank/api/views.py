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

#from .ckeditor_view import upload as ck_upload
#from .ckeditor_view import browse as ck_browse

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

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import FormView
# from .forms import SubjectiveQuestionPostForm
# from django.shortcuts import redirect

# class CkeditorSubjectiveQuestion(LoginRequiredMixin, FormView):
#     template_name = 'ckeditor_template.html'
#     form_class = SubjectiveQuestionPostForm
#
#     def form_valid(self, form):
#         user = self.request.user
#         question_html = form.cleaned_data['question_html']
#         solution_html = form.cleaned_data['solution_html']
#         try:
#             subjective_question = SubjectiveQuestion.objects.get(pk=2)
#             subjective_question.question_html = question_html
#             subjective_question.solution_html = solution_html
#             print("questionview", '*'*50, 'object craeted')
#             subjective_question.save()
#         except:
#             pass
#         return redirect('success')

# reference : https://medium.com/@adriennedomingus/working-in-forms-with-django-97ffba4206a6

# from annoying.functions import get_object_or_None
# from django.shortcuts import render
# from .forms import SubjectiveQuestionPostForm
# from .models import SubjectiveQuestion
#
#
# def ckeditor_subjective_question_edit(request, subjective_qeustion_id):
#     subjective_qeustion = get_object_or_None(SubjectiveQuestion, pk = subjective_qeustion_id)
#     if not subjective_qeustion:
#         print('error', '*'*100)
#     if request.method == "POST":
#         form = SubjectiveQuestionPostForm(request.POST, instance = subjective_qeustion)
#         if form.is_valid():
#             subjective_qeustion.save()
#     else:
#         form = SubjectiveQuestionPostForm(instance = subjective_qeustion)
#
#     context = {
#         'form' : form,
#         'subjective_question' : subjective_qeustion
#     }
#     return render(request, 'ckeditor_template.html')

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
