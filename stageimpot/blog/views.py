from django.shortcuts import render
from blog.forms import *

# Create your views here.

def loginStage(request):
    template = 'loginStage.html'
    logForm = loginStageForm()
    context = {
        'loginForm':logForm,
    }
    return render(request,template,context)

def inscriptionStage(request):
    template= 'inscriptionStage.html'
    return render(request,template)