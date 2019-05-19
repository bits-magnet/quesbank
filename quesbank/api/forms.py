from django import forms
from .models import SubjectiveQuestion


# class SubjectiveQuestionPostForm(forms.ModelForm):
#     class Meta:
#         model = SubjectiveQuestion
#         fields = ('question_html', 'solution_html')
#
#     def __int__(self, *args, **kwargs):
#
#         super(SubjectiveQuestionPostForm, self).__init__(*args, **kwargs)
#         if not self.instance:
#             self.fields['question_html'].initial = 'enter question'
#         self.fields['solution_html'].initial = 'enter solution'
#
#     def clean_time(self):
#         undated_at = self.cleaned_data['updated_at']
#         # do stuff with the time to put it in UTC based on the user's default timezone and data passed into the form.
#
#     def save(self, *args, **kwargs):
#         subjecitve_question = super(SubjectiveQuestionPostForm, self).save(*args, **kwargs)
#         return subjecitve_question
