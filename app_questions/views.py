from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponse

from .models import Article, Question
import random

def home(request):
    return render(request, 'home.html')

def questionaire(request):
    id = request.article_id
    article = Article.objects.get(id)
    questions = Question.objects.all().filter(article=article)
    return render(request, 'flipper.html', {'questions':questions})

def ajax_test(request):
    return HttpResponse(status=200)

# TODO: add question.answer, user_profile.score
def answer(request):
    try:
        question_id = request.question_id
        question = Question.objects.get(id=question_id)
        user_profile = request.user.profile
        # will only process 0, 1, or 2
        if not isinstance(request.answer, int) and request.answer > 2 or request.answer < 0:
            return HttpResponse(status=400)
        elif request.answer is question.answer:
            user_profile.score += 1
            request.user.save()
            return HttpResponse(status=200)
    except:
        return HttpResponse(status=500)

def decrement_points(request):
    user_profile = request.user.profile
    user_profile.score -= 1
    request.user.save()
    foods = Food.objects.all()
    food = random.choice(foods)
    return render(request, 'flipper.html', {'food':food})