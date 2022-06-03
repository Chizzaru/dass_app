from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    usertype = models.IntegerField()


class Question(models.Model):
    question_text = models.CharField(max_length=255)

class Choice(models.Model):
    choice_value = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)

class Answer(models.Model):
    name = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date_answered = models.DateTimeField('date answered')

class Result(models.Model):
    name = models.CharField(max_length=200, default='Name')
    score = models.IntegerField(default=0)
    depression = models.CharField(max_length=200)
    anxiety = models.CharField(max_length=200)
    stress = models.CharField(max_length=200)
    date = models.DateTimeField('date')