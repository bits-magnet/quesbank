from django.contrib import admin
from .models import *

from django.contrib import admin
from .models import *


class StandardAdmin(admin.ModelAdmin):
    list_display  = ('standard', )


class InQuestionAdmin(admin.ModelAdmin):
    list_display = ('topic', 'question_id', 'question_html')
    search_fields = ['question_html']
    list_filter = ('topic__subject__subject', 'topic', )


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('type', 'updated_at', 'inquestion')
#     search_fields = ['inquestion__question_html']
#     # list_filter = ()


class SubjectiveQuestionAdmin(admin.ModelAdmin):
    list_display = ( 'question_html', 'solution_html')
    search_fields = ['question_html']
    list_filter = ('question_type', 'topic' )


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('standard', 'subject')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic_id', 'topic')
    list_filter = ['subject__subject']
    search_fields = ['topic']


admin.site.register(Standard, StandardAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(InQuestion, InQuestionAdmin)
admin.site.register(Question)
admin.site.register(ObjectiveQuestion)
admin.site.register(SubjectiveQuestion, SubjectiveQuestionAdmin)
admin.site.register(SimilarSubjectiveQuestion)
admin.site.register(SimilarObjectiveQuestion)
admin.site.register(ArchievedSubjectiveQuestion)
