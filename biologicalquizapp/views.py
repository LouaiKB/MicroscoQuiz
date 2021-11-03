from random import randint, shuffle
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Answer, Image, Question
from django.views import View

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
    }
    return render(request, 'biologicalquizapp\quiz.html', context)

@login_required
def microscopy_quiz(request):
    images_and_answer = Image.get_random_images('mode', 3)
    context = {}
    context['title'] = 'microscopy quiz'
    context['question_1'] = Question.objects.filter(id=1).values()[0]['question']
    context['data'] = []
    num = 1
    for element in images_and_answer:
        answers = Answer.generate_random_answers(1)
        correct_answer = list(element.keys())[0]
       
        if correct_answer not in answers:
            answers[-1] = correct_answer

        shuffle(answers)
        context['data'].append({
            'num': num,
            'images': ["data\\" + str(i.name) + ".jpg" for i in element[list(element.keys())[0]]],
            'answers': answers,
            'correct_answer': correct_answer,
            'description': Answer.objects.filter(answer=correct_answer).values()[0]['definition']
        })
        num += 1
    return render(request, 'biologicalquizapp\microscopy_quiz.html', context)
 
@login_required
def features_quiz(request):
    # we will pick up random question from celltype or components
    # random_num = randint(1, 2)
    
    # if 1 we will choose the components questions
    # if random_num == 1:
    images_and_answer = Image.get_random_images('components', 2)

    # elif random_num == 2:
    #     images_and_answer = Image.get_random_images('celltype', 2)

    context = {}
    context['title'] = 'features quiz'
    context['question_2'] = Question.objects.filter(id=2).values()[0]['question']
    context['data'] = []
    num = 1
    for element in images_and_answer:
        answers = Answer.generate_random_answers(2)
        correct_answer = list(element.keys())[0]
       
        if correct_answer not in answers:
            answers[-1] = correct_answer

        shuffle(answers)
        context['data'].append({
            'num': num,
            'images': ["data\\" + str(i.name) + ".jpg" for i in element[list(element.keys())[0]]],
            'answers': answers,
            'correct_answer': correct_answer,
            'description': Answer.objects.filter(answer=correct_answer).values()[0]['definition']
        })
        num += 1
    

    return render(request, 'biologicalquizapp\\feature_quiz.html', context)