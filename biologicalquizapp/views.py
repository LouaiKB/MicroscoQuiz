from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Answer, Image, Question

# Create your views here.
def home(request):
    context = {
        'title' : 'home'
    }
    return render(request, 'biologicalquizapp\home.html', context)

@login_required
def quiz_view(request):
    context = {
        'title': 'quiz page',
        'question_1': Question.objects.filter(id=1).values()[0]['question'],
        'question_2': Question.objects.filter(id=2).values()[0]['question'],
        'answer_1': Answer.objects.filter(question_id=1).values(),
        'answer_2': Answer.objects.filter(question_id=2).values(),
        'images': ["data\\" + str(i.name) + ".jpg" for i in Image.get_random_images('celltype', 2)]
    }
    return render(request, 'biologicalquizapp\quiz.html', context)