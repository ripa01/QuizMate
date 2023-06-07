from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string
from ckeditor.fields import RichTextField


class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='teacherAtClass', on_delete=models.CASCADE)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='classs', blank=True)

    def save(self, *args, **kwargs):
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        while self.code is None:
            temp = get_random_string(6, allowed_chars=a)
            if Class.objects.filter(code=temp).exists():
                continue
            else:
                self.code = temp
                break
        super(Class, self).save(*args, **kwargs)    

    def __str__(self):
        return str(self.id) + ": " + self.name




class Exam(models.Model):
    classes = models.ForeignKey(Class, related_name='exams', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField(default=None)
    start_time = models.TimeField(default=None)
   
    duration = models.IntegerField(default=60, null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Exam, self).save(*args, **kwargs)

class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    QUESTION_TYPE = (
        ('SingleMCQ', 'SingleMCQ'),
        ('MultipleMCQ', 'MultipleMCQ'),
        ('TrueFalse', 'TrueFalse'),
        ('Subjective', 'Subjective'),
    )
    question = models.TextField()
    question_type = models.CharField(max_length=100, choices=QUESTION_TYPE)
    mark = models.IntegerField(default=1)
    options = models.ManyToManyField('Option', related_name='questions', blank=True)
    def __str__(self):
        return self.question

class Option(models.Model):
    option = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option



class AnswerSheet(models.Model):
    STATUS_TYPE = (
        ('NOT_STARTED', 'NOT_STARTED'),
        ('STARTED', 'STARTED'),
        ('SUBMITTED', 'SUBMITTED'),
    )
    exam = models.ForeignKey(Exam, related_name='answer_sheets', on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answersheets', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_TYPE, default='NOT_STARTED')
    mark = models.IntegerField(default=0, null=True, blank=True)
    total_marks = models.IntegerField(default=0, null=True, blank=True)
    percentage = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.student.username

class Answer(models.Model):
    answersheet = models.ForeignKey(AnswerSheet, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    mark = models.IntegerField(default=(1 if is_correct else 0))
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.answer