from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(read_only=True)
    topic = TopicSerializer(source='topic_set', many=True)
    class Meta:
        model = Subject
        depth = 1
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
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


class SimilarSubjectiveQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    class Meta:
        model = SimilarSubjectiveQuestion
        fields = '__all__'


class SimilarObjectiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarObjectiveQuestion
        fields = '__all__'
