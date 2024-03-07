from django.forms import ModelForm
from django import forms
from .models import *
class loginStageForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}),error_messages={'required':'champ obligatoire'})
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control login-input'}),error_messages={'required':'champ obligatoire'})

class UserStageForm(forms.Form):
    username = forms.CharField(label='username', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input','placeholder':'roova-24'}),error_messages={'required':'champ obligatoire'})    
    password = forms.CharField(label='Mot de passe', max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control login-input'}),error_messages={'required':'champ obligatoire'})    
    nom = forms.CharField(label='Nom', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}),error_messages={'required':'champ obligatoire'})    
    prenom = forms.CharField(label='Prenom', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}),error_messages={'required':'champ obligatoire'})
    email = forms.CharField(label='Email', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}),error_messages={'required':'champ obligatoire'})    

class UserStageComplete(forms.Form):    
    date_de_naissance = forms.DateField(label='Date de naissance', widget=forms.DateInput(attrs={'type':'date','placeholder':'JJ/MM/AAAA','class':'form-control login-input'}))
    telephone = forms.CharField(label='Telephone', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    adresse = forms.CharField(label='Adresse', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))    
    filiere = forms.CharField(label='Filiere', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    

class demandeStageForm(forms.Form):        
    projet = forms.CharField(label='Projet', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    lettre_de_motivation = forms.CharField(label='Lettre de Motivation', max_length=200, widget=forms.Textarea(attrs={'class':'form-control'}))
    filename = forms.FileField(label='CV', max_length=200, widget=forms.FileInput(attrs={'class':'form-control login-input'}))
    


