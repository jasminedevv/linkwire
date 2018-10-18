from django.test import TestCase
from .views import answer
from django.http import HttpResponse

# Create your tests here.

def test_answer():
    request = HttpResponse()
    request.path = "/answer/?article=0&question=0&answer=0"
    assert answer(request).status_code is 200
