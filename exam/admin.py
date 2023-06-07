from django.contrib import admin
from exam.models import Class, Exam, Question, Option, AnswerSheet, Answer
# Register your models here.

admin.site.register(Class)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(AnswerSheet)
admin.site.register(Answer)