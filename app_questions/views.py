from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.http import HttpResponse

from .models import Article, Question, Score
from django.contrib.auth.models import User
import random

from termcolor import colored

class TermColors():
    def format(self, input, color):
        output = str(input)
        print(colored("log: " + output, color))
    def red(self, output):
        self.format(output, 'red')
    def pink(self, output):
        self.format(output, 'magenta')
    def green(self, output):
        self.format(output, 'green')
    def white(self, output):
        self.format(output, 'white')

log = TermColors()
    
def get_user_by_id(id):
    user = User.objects.get()
    return user

def home(request):
    user = request.user
    articles = Article.objects.all()
    if user.is_authenticated:
        return render(request, 'home.html', {'user':user, 'articles':articles})
    else:
        return redirect('accounts/login/')

def questionaire(request):
    id = request.article_id
    article = Article.objects.get(id)
    questions = Question.objects.all().filter(article=article)
    return render(request, 'flipper.html', {'questions':questions})

def ajax_test(request):
    return HttpResponse(status=200)

# TODO: user_profile.score
def answer(request):
    log.white("CHECKING ANSWER")
    question_id = request.GET.get('article')
    log.white("Question ID registered: "+question_id)
    try:
        question = Question.objects.get(id=question_id)
    except:
        return HttpResponse(status=404, content="Cannot retrieve question.")
    try:
        answer = int( request.GET.get('answer') )
        log.white("Received answer: "+ str( answer )  )
    except:
        return HttpResponse(status=400, content="Answer needs to be a number.")
    # will only process 0, 1, or 2
    if not isinstance(answer, int) and answer > 2 and answer < 0:
        return HttpResponse(status=400, content="Invalid answer number.")
    else:
        try:
            log.pink(request.user.username)
            log.pink(request.user.score.total_right)
            # user_stats = Score.objects.get(user=request.user)
            # log.white(user_stats.score)
        except:
            return HttpResponse(status=501, content="I could not find a score for that user :(")

    if answer is question.answer:
        log.green("ANSWER CORRECT")
        request.user.score.total_right += 1
        request.user.score.save()
        return HttpResponse(status=200, content="Answer correct.")
    else:
        log.red("ANSWER INCORRECT")
        request.user.score.total_wrong -= 1
        request.user.score.save()
        return HttpResponse(status=200, content="Answer incorrect.")