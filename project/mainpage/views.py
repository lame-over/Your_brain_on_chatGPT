from django.shortcuts import render
from questions.models import *

# Create your views here.
def mainpage(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'mainpage/index.html', context)