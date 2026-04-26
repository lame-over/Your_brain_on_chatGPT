from django.shortcuts import render
from questions.models import *

# Create your views here.
def questions(request):
    context = {
        'questions': Question.objects.all(),
        'character': Character.objects.all()
    }
    return render(request, 'quest/quest.html', context)