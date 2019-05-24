from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField


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
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    question_id = models.CharField(default='NA', max_length=100)
    question_html = RichTextUploadingField()
    solution_html = RichTextUploadingField()
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
    question_level = models.IntegerField(default=0)

    def __str__(self):
        return self.question_html


class Question(models.Model):
    CHOICES = [
        ('created', 'created'),
        ('imported', 'imported'),
        ('processed', 'processed'),
        ('duplicate', 'duplicate'),
        ('rejected', 'rejected'),
        ('approved', 'approved')
    ]
    inquestion = models.ForeignKey(InQuestion, on_delete=models.CASCADE)
    question_type = models.CharField(default='NA', max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, choices=CHOICES, default=CHOICES[0])
    level = models.IntegerField(default=0)
    length = models.CharField(default='', max_length=25)

    def __str__(self):
        return self.state


class SubjectiveQuestion(Question):
    question_html = RichTextUploadingField()
    solution_html = RichTextUploadingField()

    def __str__(self):
        return self.question_html


class ObjectiveQuestion(Question):
    question_html = RichTextUploadingField()
    solution_html = RichTextUploadingField()
    options = ArrayField(RichTextUploadingField(), blank=True, null=True)
    correct_option = models.CharField(default='', max_length=500, null=True)

    def __str__(self):
        return self.question_html


class SimilarSubjectiveQuestion(models.Model):
    question = models.ForeignKey(SubjectiveQuestion,  related_name='question', on_delete= models.CASCADE)
    similar_to_question = models.ForeignKey(SubjectiveQuestion, related_name='similar_to_question', on_delete=models.CASCADE)
    similarity_percentage = models.IntegerField(default=0)

    def __str__(self):
        return str(self.question.id) + " "+ str(self.similar_to_question.id)


class SimilarObjectiveQuestion(models.Model):
    question = models.ForeignKey(ObjectiveQuestion, related_name='question', on_delete= models.CASCADE)
    similar_to_question = models.ForeignKey(ObjectiveQuestion, related_name='similar_to_question' , on_delete=models.CASCADE)
    similarity_percentage = models.IntegerField(default=0)

    def __str__(self):
        return str(self.question.id) + " "+ str(self.similar_to_question.id)


class ArchievedSubjectiveQuestion(models.Model):
    CHOICES = [
        ('created', 'created'),
        ('imported', 'imported'),
        ('processed', 'processed'),
        ('duplicate', 'duplicate'),
        ('rejected', 'rejected'),
        ('approved', 'approved')
    ]
    inquestion = models.ForeignKey(InQuestion, on_delete=models.CASCADE)
    question_type = models.CharField(default='NA', max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, choices=CHOICES, default=CHOICES[0])
    level = models.IntegerField(default=0)
    length = models.CharField(default='', max_length=25)
    question_html = RichTextUploadingField()
    solution_html = RichTextUploadingField()


class ArchievedObjectiveQuestion(models.Model):
    CHOICES = [
        ('created', 'created'),
        ('imported', 'imported'),
        ('processed', 'processed'),
        ('duplicate', 'duplicate'),
        ('rejected', 'rejected'),
        ('approved', 'approved')
    ]
    inquestion = models.ForeignKey(InQuestion, on_delete=models.CASCADE)
    question_type = models.CharField(default='NA', max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, choices=CHOICES, default=CHOICES[0])
    level = models.IntegerField(default=0)
    length = models.CharField(default='', max_length=25)
    question_html = RichTextUploadingField()
    solution_html = RichTextUploadingField()
    options = ArrayField(RichTextUploadingField(), blank=True, null=True)
    correct_option = models.CharField(default='', max_length=500, null=True)

    def __str__(self):
        return self.question_html

