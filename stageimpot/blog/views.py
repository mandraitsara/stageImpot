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
    stageForm = stageDemandeForm()    
    template= 'inscriptionStage.html'
    context = {
        'stageform':stageForm
    }
    return render(request,template, context)