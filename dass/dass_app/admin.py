from django.contrib import admin
from .models import Question, Choice, Answer, Result

class QuestionList(admin.ModelAdmin):
    list_display= ('id', 'question_text')

class ChoiceList(admin.ModelAdmin):
    list_display= ('id','choice_value','choice_text')

class AnswerList(admin.ModelAdmin):
    list_display= ('id','name','question','answer','date_answered')

class ResultList(admin.ModelAdmin):
    list_display= ('id','name','score','depression','anxiety','stress','date')

# Register your models here.
admin.site.register(Question, QuestionList)
admin.site.register(Choice, ChoiceList)
admin.site.register(Answer, AnswerList)
admin.site.register(Result, ResultList)