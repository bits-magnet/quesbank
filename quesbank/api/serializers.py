from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class InQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InQuestion
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SubjectiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectiveQuestion
        fields = '__all__'


class ObjectiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectiveQuestion
        fields = '__all__'
