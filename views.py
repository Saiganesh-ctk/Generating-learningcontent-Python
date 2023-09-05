import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import overview
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "/Users/saiganeshthamaraikannan/Desktop/django/template_mini_project/django/myproject/firstapp/gpt3")
model = AutoModelForCausalLM.from_pretrained(
    "/Users/saiganeshthamaraikannan/Desktop/django/template_mini_project/django/myproject/firstapp/gpt3")


def home(request):
    return render(request, 'index.html', {'ans': 'overview will be here', 'question': 'questions will be here.'})


def submit(request):
    ans = {'ans': 'overview will be here.....',
           'question': 'questions will be here...'}
    if request.method == 'POST':
        ans = request.POST['area']
        if ans.strip() == '':
            ans = {'ans': 'overview will be here.....',
                   'question': 'questions will be here...'}
        else:
            learning_resources = ans.split('$')
            over, questions = overview(learning_resources)
            ans = {'ans': over, 'question': questions}
    return render(request, 'index.html', ans)
