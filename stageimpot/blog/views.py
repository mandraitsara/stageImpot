from django.shortcuts import render,redirect
from blog.forms import *
from blog.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #pour manipuler l'ajax
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models.functions import Coalesce

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
                    # stagiaires_id = demandeStage.objects.filter(user_id__exact=user_id)
                    # print(stagiaires_id)
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
    list_users = demandeStage.objects.all()
    print(list_users)
    context = {
        "list_users":list_users,
    }
    return render(request, template,context)  

def compteStagiaire(request):
    template = "gestionStage.html"
    # demandestage= demandeStage.objects.all()    
    completeUserModel = userCompleteModel.objects.all()   
    demandestage = demandeStageForm(request.POST, request.FILES)
    stagiaires = demandeStage.objects.order_by(Coalesce('dates','projet').desc())
    
    
    page = request.GET.get('page',1)

    paginator = Paginator(stagiaires,10)
    

    try:
        page_obj= paginator.page(page)
        print('page...'+str(page_obj))
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    


   
    
    
    # val = ""

    # for usercomplete in completeUserModel:
    #     val +=  str(usercomplete.id)
    
    # if val == 3:
    #     print('je taime')
    # print(val) 
        
       

    # completeUserForm = UserStageComplete()
    context = {
        'demandestage':demandestage,
        'completeUserModel':completeUserModel,
        'stagiaires':stagiaires,
        'page_obj':page_obj,
        # 'completeUserForm':completeUserForm,
    }

    
    return render(request,template,context)


def detailStage(request, id):
    template = 'detailStage.html'
    users_id = User.objects.get(id=id)
    complete_id = userCompleteModel.objects.get(user_id=users_id)
    demande_id = demandeStage.objects.filter(user_id=users_id)
    directions = directionUser.objects.all()

    context = {
        'idStage':users_id,
        'complete_id':complete_id,
        'directions':directions,
        'demande_id':demande_id

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
        if completeUserForm.is_valid():
            user = request.POST['user_id']
            date_de_naissance = request.POST['date_de_naissance']
            filiere = request.POST['filiere']
            telephone = request.POST['telephone']
            stage_complete = userCompleteModel(user_id=user,date_de_naissance=date_de_naissance,filiere=filiere,telephone=telephone)
            stage_complete.save()        
            return redirect('comptestagiaire')
        else:
            return render(request, 'userComplete.html',context)        
    return render(request, 'userComplete.html',context)

#@csrf_exempt
def demandestage(request):
    if request.method == 'POST':
        stage = demandeStageForm(request.POST, request.FILES)
        if stage.is_valid():
            user_id = request.POST['user_id']
            projet = request.POST['projet']
            lettre_de_motivation = request.POST['lettre_de_motivation']
            filename = request.FILES['filename']
            print(user_id)
            print(filename)
            demande = demandeStage(user_id=user_id,projet=projet,lettre_de_motivation=lettre_de_motivation,fichier=filename)
            demande.save()
        return redirect('comptestagiaire')
    return redirect('comptestagiaire')
    
    #     messageR = 'enregistrement effectué'
    #     messageE = 'enregistrement echoué' content = {
    #         'result':messageR,
    #         'result':messageE
    #             }    

    # user_id = request.POST.get('user_id')
    # projet = request.POST.get('projet')
    # lettre_de_motivation = request.POST.get('lettre_de_motivation')
    # filename = request.FILES.get('filename')
    # print('testf  '+ str(filename))
    # demande = demandeStage(user_id=user_id,projet=projet,lettre_de_motivation=lettre_de_motivation,fichier=filename)

    # return JsonResponse({'result':'salut'})
    #save = demande.save()

   #if save:
   #     return JsonResponse({'result':messageE})   
   # else:
   #     return JsonResponse({'result':messageR})

def noteStage(request):
    if request.method=='POST':    
        idClients = request.POST['idStage']
        EditClients = demandeStage.objects.get(user_id=idClients)
        observation = request.POST['obs']
        directions = request.POST['direct']

        EditClients.observation = observation        
        EditClients.departement = directions
        EditClients.save()
        print('enregistrement effectué..')

        #print('j\'affiche le numero de user : ' + str(EditClients.user_id))
        return redirect('superadmin')

    return redirect('superadmin')