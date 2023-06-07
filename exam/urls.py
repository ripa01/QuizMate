from django.urls import path, include
from django.views.generic import TemplateView

from .views import classView, examStart, homeView, examDetailsView, examView,reportcardView

urlpatterns = [
    
    path('', homeView, name='home'),
    path('class/<str:class_code>/', classView, name='classDetails'),
    path('exam/details/<int:exam_code>', examDetailsView, name='examDetailsView'),
    path('exam/start/<int:exam_id>/', examStart, name='examStart'),
    path('exam/<int:exam_id>/', examView, name='exam'),
    path('exam/<int:exam_id>/reportcard', reportcardView, name='reportcard'),
    path('exam/<int:exam_id>/reportcard/<int:student_id>', reportcardView, name='reportcard'),
    
]
