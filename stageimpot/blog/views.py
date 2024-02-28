from django.shortcuts import render,redirect
from blog.forms import *
from blog.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def loginStage(request):
    template = 'loginStage.html'
    logForm = loginStageForm(request.POST)
    context = {
        'loginForm':logForm,
    }
    if request.method == "POST":
        if logForm.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if user.is_superuser == True:
                    return redirect('superadmin')
                else:
                    user_id = user.id
                    id_user = userCompleteModel.objects.filter(user_id__exact=user_id)                   
                    
                    if id_user:
                        return redirect('comptestagiaire')
                    else:
                        return redirect('completestage')
        else:
            messages.error(request, "authentification échoué")
            for field in logForm.errors:
                logForm['field'].field.widget.attrs['class']+="is-invalid"
            return render(request, template, context)

    return render(request,template,context)

def inscriptionStage(request):
    stageForm = UserStageForm(request.POST)    
    template= 'inscriptionStage.html'  

    context = {
        'stageform':stageForm
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        try:
            user_exist = User.objects.get(username=username,email=email)            
        except:
            print('')
        if len(username)<2:
            messages.error(request, 'Erreur nom')
            return render(request,template, context)
        if stageForm.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            email = request.POST['email']
            user = User.objects.create_user(first_name=nom,last_name=prenom,username=username,email=email,password=password)
     
            if user is not None:
                return redirect('loginstage')
            else:
                messages.error(request,'USER - Enregistrement échoué...!')
                return render(request,template, context)

        else:
            for field in stageForm.errors:
                stageForm[field].field.widget.attrs['class'] += " is-invalid "
            return render(request,template, context)
            
    else:
        messages.error(request, "authentification echoué...")
        return render(request,template, context)
    
    return render(request,template, context)

def superAdmin(request):
    template = "gestionAdmin.html"
    list_users = User.objects.all()
    context = {
        "list_users":list_users,
    }
    return render(request, template,context)

def compteStagiaire(request):
    template = "gestionStage.html"
    demandestage= demandeStage.objects.all()
    completeUserModel = userCompleteModel.objects.all()   
    
    
    # val = ""

    # for usercomplete in completeUserModel:
    #     val +=  str(usercomplete.id)
    
    # if val == 3:
    #     print('je taime')
    # print(val) 
        
       

    completeUserForm = UserStageComplete()
    context = {
        'demandestage':demandestage,
        'completeUserModel':completeUserModel,
        'completeUserForm':completeUserForm,
    }

    
    return render(request,template,context)


def detailStage(request, id):
    template = 'detailStage.html'
    users_id = User.objects.get(id=id)  

    context = {
        'idStage':users_id,       

    }
    
    return render(request,template,context)

def logoutStage(request):
    logout(request)
    return redirect('loginstage')

def completeStage(request):
    completeUserForm = UserStageComplete(request.POST)
    context = {
        'completeUserForm':completeUserForm
    }
    if request.method == 'POST':
        user = request.POST['user_id']
        date_de_naissance = request.POST['date_de_naissance']
        filiere = request.POST['filiere']
        telephone = request.POST['telephone']
        stage_complete = userCompleteModel(user_id=user,date_de_naissance=date_de_naissance,filiere=filiere,telephone=telephone)
        saves_user = stage_complete.save()
        if saves_user:
            return redirect('comptestagiaire')
    return render(request, 'userComplete.html',context)

