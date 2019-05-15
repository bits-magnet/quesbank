from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


class Standard(models.Model):
    standard = models.IntegerField(default=0)

    def __str__(self):
        return str(self.standard)


class Subject(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject = models.CharField(default='', max_length= 100)

    def __str__(self):
        return self.subject


class Source(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    source_name = models.CharField(default='', max_length=100)
    source_type = models.CharField(default='JSON file', max_length= 100)

    def __str__(self):
        return self.source_name


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    topic = models.CharField(default='', max_length= 200)
    topic_id = models.IntegerField(default=0)

    def __str__(self):
        return self.topic


class InQuestion(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_id = models.CharField(default='NA', max_length=100)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    question_html = models.TextField(default='NA')
    solution_html = models.TextField(default='NA')
    is_publish = models.CharField(default='NA', max_length=10)
    is_active = models.CharField(default='NA', max_length=10)
    tc_map_id = models.CharField(default='NA', max_length=100)
    text_book_id = models.CharField(default='NA', max_length=100)
    chapter_id = models.CharField(default='NA', max_length=100)
    exercise_id = models.CharField(default='NA', max_length=100)
    flow = models.CharField(default='NA', max_length=100)
    set_no = models.CharField(default='NA', max_length=100)  # science
    page_flow = models.CharField(default='NA', max_length=100)
    page_no = models.CharField(default='NA', max_length=100)
    question_no = models.CharField(default='NA', max_length=100)
    exercise_flow = models.CharField(default='NA', max_length=100)
    edition = models.CharField(default='NA', max_length=100)
    tc_map_is_active = models.CharField(default='', max_length=10)
    slo_id = models.CharField(default='NA', max_length=100)
    slo_map_id = models.CharField(default='NA', max_length=100)
    slo_mao_is_active = models.CharField(default='', max_length=10)
    exercise_name = models.CharField(default='NA', max_length=150)


class Question(models.Model):
    inquestion = models.ForeignKey(InQuestion, on_delete=models.CASCADE)
    type = models.CharField(default='NA', max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    state = models.CharField(default='imported', max_length=50)
    level = models.IntegerField(default=0)
    length = models.CharField(default='', max_length=25)

    def __str__(self):
        return self.question_id


class SubjectiveQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_html = models.CharField(default='', max_length=10000)
    solution_html = models.CharField(default='', max_length=10000)

    def __str__(self):
        return self.question_html


class ObjectiveQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_html = models.CharField(default='', max_length=10000)
    solution_html = models.CharField(default='', max_length=10000)
    options = ArrayField(models.CharField(max_length=500), blank=True)
    correct_option = models.CharField(max_length=500)

    def __str__(self):
        return self.question_html


# class FillInTheBlanksQuestion(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     question_html = models.CharField(default='', max_length=10000)
#     solution_html = models.CharField(default='', max_length=10000)
#     correct_answer = models.CharField(default='', max_length=1000)
