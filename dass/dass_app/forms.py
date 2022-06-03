from django import forms
from .models import Users, Question, Choice

class DassForm(forms.Form):
    myQuestions = Question.objects.all().values()
    myChoices = Choice.objects.all().values()
    for x in myQuestions:
        question = forms.CharField(label = 'tr', max_length=100)