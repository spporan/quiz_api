from django.urls import path

from quiz import views

urlpatterns = [
    path('',views.getQuizApi, name='quiz'),
    path('r/<str:topic>/',views.getRandomQuestion, name='question'),
    path('questions',views.getQuestions, name='questions')


]