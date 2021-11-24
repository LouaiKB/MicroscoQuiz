from random import shuffle
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Answer, Image, Question
from users.models import Profile
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    context = {
        'title' : 'home'
    }
    return render(request, 'biologicalquizapp/home.html', context)

@login_required
def quiz_view(request):
    context = {
        'title': 'quiz page',
        'question_1': Question.objects.filter(id=1).values()[0]['question'],
        'question_2': Question.objects.filter(id=2).values()[0]['question'],
    }
    return render(request, 'biologicalquizapp/quiz.html', context)

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
            'images': ["data/" + str(i.name) + ".jpg" for i in element[list(element.keys())[0]]],
            'answers': answers,
            'correct_answer': correct_answer,
            'description': Answer.objects.filter(answer=correct_answer).values()[0]['definition']
        })
        num += 1

    return render(request, 'biologicalquizapp/microscopy_quiz.html', context)

@login_required
@csrf_exempt
def microscopy_quiz_save(request):
    print("microsco quiz save")
    if request.is_ajax():
        print("inside ajax")
        score_user = request.POST['score']
        user = request.user
        current_user = Profile.objects.filter(user=user.id)
        score = current_user.get().microscopy_score + int(score_user)
        total_score = current_user.get().total_score + score
        current_user.update(microscopy_score = score)
        current_user.update(total_score = total_score)

        if total_score > 80 and total_score < 180:
            current_user.update(level = 'intermediate')
        elif total_score > 180:
            current_user.update(level='advanced')

    else:
        html = "error"
        print("ERROR: ", html)

@login_required
@csrf_exempt
def features_quiz_save(request):
    print("features quiz save")
    if request.is_ajax():
        print("inside ajaxxxxx")
        score_user = request.POST['score']
        user = request.user
        current_user = Profile.objects.filter(user=user.id)
        score = current_user.get().component_score + int(score_user)
        total_score = current_user.get().total_score + score
        current_user.update(component_score = score)
        current_user.update(total_score = total_score)

        if total_score > 80 and total_score < 180:
            current_user.update(level = 'intermediate')
        elif total_score > 180:
            current_user.update(level='advanced')

    else:
        html = "error"
        print("ERROR: ", html)



@login_required
def features_quiz(request):
    images_and_answer = Image.get_random_images('components', 2)
    
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
            'images': ["data/" + str(i.name) + ".jpg" for i in element[list(element.keys())[0]]],
            'answers': answers,
            'correct_answer': correct_answer,
            'description': Answer.objects.filter(answer=correct_answer).values()[0]['definition']
        })
       
        num += 1
    
    return render(request, 'biologicalquizapp/feature_quiz.html', context)

class ExplorePage(ListView):
    
    template_name = 'biologicalquizapp/explore.html'
    model = Image
    context_object_name = 'images'
    paginate_by = 10
    queryset = Image.objects.all()

    def get_context_data(self, **kwargs):
        context =  super(ExplorePage, self).get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        context['title'] = 'explore page'
        context['metadatas'] = Image.get_metadatas()
        return context

def explore_page(request):
    images_list = Image.objects.all()
    paginator = Paginator(images_list, 10)
    page = request.GET.get('page', 1)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    context = {
        'title': 'explore page',
        'images' : images,
        'metadatas': Image.get_metadatas(),
        'paginated' : True,
        'paginator': paginator,
        'page_number': int(page),
    }

    return render(request, 'biologicalquizapp/explore.html', context)


class ExploreImage(DetailView):
    model = Image


def search(request):
    query = request.GET.get('query')
   
    if not query:
        images_list = Image.objects.all()
        paginator = Paginator(images_list, 10)
        page = request.GET.get('page', 1)
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)

        context = {
            'paginated': True, 
            'paginator': paginator,
            'page_number': int(page)
        }

    else:
        images = Image.objects.filter(mode__icontains=query)
        
        if not images.exists():
            images = Image.objects.filter(components__icontains=query)

        if not images.exists():
            images = Image.objects.filter(organism__icontains=query)
        
        if not images.exists():
            images = Image.objects.filter(celltype__icontains=query)
        
    context = {
        'images': images,
        'metadatas': Image.get_metadatas()          
    }
    return render(request, 'biologicalquizapp/explore.html', context)

@login_required
def ranking_page(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'biologicalquizapp/ranking_page.html', context)
