from django.shortcuts import render, redirect
from questions.models import *
from character.models import *
from character.forms import Character_create_form

# Create your views here.
def mainpage(request):
    context = {
        
        'character_form': Character_create_form(),
    }


    if request.method == "POST":
        form = Character_create_form(request.POST)
        
        if form.is_valid():
            name = "Name"
            character = Character(name=name)
            character.save()
            return redirect('info/')
    
    return render(request, 'mainpage/index.html', context)

def info(request):
    context = {
        'questions': Question.objects.first(),
    }

    print(context['questions'].description)

    if request.method == "POST":
        return redirect('/quest')
    
    return render(request, 'mainpage/info.html', context)