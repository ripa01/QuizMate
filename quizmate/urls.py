
from django.contrib import admin
from django.urls import path, include
from exam.views import landingPage, loginView, logoutView, registrationView,changeView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', landingPage, name='landing'),
    path('register/', registrationView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('change/',changeView,name = 'change'),
    path('admin/', admin.site.urls),
    path('home/', include('exam.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/', loginView, name='login'),


 
  

]


