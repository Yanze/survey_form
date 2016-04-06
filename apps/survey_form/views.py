from django.shortcuts import render, redirect
from apps.survey_form.models import Form
from django.core.exceptions import ValidationError

# Create your views here.
context = {}
def index(request):
    global context
    temp = context
    context = {}
    return render(request, 'survey/index.html', temp)

def add(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            if "counter" not in request.session:
                request.session['counter'] = 1
            else:
                request.session['counter'] += 1

            request.session['name'] = form.cleaned_data['name']
            request.session['location'] = form.cleaned_data['location']
            request.session['language'] = form.cleaned_data['language']
            request.session['comment'] = form.cleaned_data['comment']
            return redirect('/show')
        else:
            global context
            context = {
                'error': 'Inputs cannot be blank.'
            }
            return redirect('/')


def show(request):
    context = {
        'counter': request.session['counter'],
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
    }
    return render(request, 'survey/show.html', context)
