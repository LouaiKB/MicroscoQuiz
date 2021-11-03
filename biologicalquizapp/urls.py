from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('quizapp/', views.quiz_view, name='quiz-view'),
    path('quizapp/microscopy_quiz/', views.microscopy_quiz, name='microscopy-quiz'),
    path('quizapp/features_quiz/', views.features_quiz, name='features-quiz')
]
