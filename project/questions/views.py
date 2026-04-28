from django.shortcuts import render, redirect
from questions.models import *
from character.models import *
from character.forms import Character_update_form

# Question.objects.count() - общее количество вопросов в базе данных
# Счетчик для определения текущего вопроса, который отображается на странице


def start_game(input_value = 0):
    input_value += 1
    return input_value

def questions(request):

    button_pressed = None
    social_life_input = None
    grade_input = None
    dependence_input = None
    values = {}
    form = None

    questions_count = Character.objects.last().count_for_question

    context = {
        'character': Character.objects.last(),
        'questions': Question.objects.get(index=questions_count),
        'decisions': Decision.objects.filter(question_index= Question.objects.get(index=questions_count),
        ),
    }

    print(context['character'].grade)
    print(context['character'].dependence)
    print(context['character'].social_life)

    for decision in context['decisions']:
        decision.is_available = False
        decision.save()

    for decision in context['decisions']:
        if (decision.minimal_value_for_social_life < context['character'].social_life and decision.minimal_value_for_social_life != 0) or (decision.minimal_value_for_grade < context['character'].grade and decision.minimal_value_for_grade != 0) or ((decision.minimal_value_for_dependence < context['character'].dependence and decision.minimal_value_for_dependence != 0 and decision.minimal_value_for_dependence > 0) or (decision.minimal_value_for_grade > context['character'].grade and decision.minimal_value_for_grade != 0)) or ((decision.minimal_value_for_dependence > context['character'].dependence and decision.minimal_value_for_dependence != 0 and decision.minimal_value_for_dependence < 0) or (decision.minimal_value_for_grade < context['character'].grade and decision.minimal_value_for_grade != 0)) or (decision.minimal_value_for_social_life == 0 and decision.minimal_value_for_grade == 0 and decision.minimal_value_for_dependence == 0):
            decision.is_available = True
    

    if request.method == "POST" and request.POST.get('button'):
        if request.POST.get('button'):

            # Кнопка, которую нажал пользователь, сохраняется в переменную
            button_pressed = request.POST.get('button')

            # Разделяем строку на части, используя запятую в качестве разделителя
            values = button_pressed.split(', ')
            # Почему-то у машины иногда возникает ошибка, что в массиве есть значение None, если одно из значений = 0
            if None in values:
                value[values.indexOf(None)] = 0


            # Суммируем значения из массива с соответствующими атрибутами персонажа
            social_life_input = int(values[0]) + context['character'].social_life
            grade_input = int(values[1]) + context['character'].grade
            dependence_input = int(values[2]) + context['character'].dependence
            questions_count = context['character'].count_for_question + 1

            # Запись в ДБ новых значений атрибутов персонажа
            character = Character(social_life = social_life_input, grade = grade_input, 
            dependence = dependence_input, id = context['character'].id, 
            name = context['character'].name, 
            count_for_question = questions_count)
            character.save()
            
            if questions_count == Question.objects.count():
                return redirect('ending/')
    
    return render(request, 'quest/questions.html', context)

def ending(request):
    context = {
        'character': Character.objects.last(),
        'endings': Endings.objects.all(),
    }

    print(context['character'].social_life)
    print(context['character'].grade)
    print(context['character'].dependence)

    social_life = context['character'].social_life
    grade = context['character'].grade
    dependence = context['character'].dependence

    for ending in context['endings']:
        if (social_life >= 0 and ending.social_life >= 0 and social_life > ending.social_life // 2) or (grade >= 0 and ending.grade >=0 and grade >= ending.grade // 2) or (dependence >= 0 and ending.dependence >= 0 and dependence > ending.dependence) or (dependence <= 0 and ending.dependence <= 0 and dependence < ending.dependence):
            context['endings'] = Endings.objects.get(id=ending.id)
            break

    return render(request, 'quest/final.html', context)