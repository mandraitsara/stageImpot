from django import forms

class loginStageForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control login-input'}))

class UserStageForm(forms.Form):
    username = forms.CharField(label='username', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input','placeholder':'roova-24'}))    
    password = forms.CharField(label='Mot de passe', max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control login-input'}))    
    nom = forms.CharField(label='Nom', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))    
    prenom = forms.CharField(label='Prenom', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    email = forms.CharField(label='Email', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))    

class UserStageComplete(forms.Form):    
    date_de_naissance = forms.DateField(label='Date de naissance', widget=forms.DateInput(attrs={'type':'date','placeholder':'JJ/MM/AAAA','class':'form-control login-input'}))
    telephone = forms.CharField(label='Telephone', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    adresse = forms.CharField(label='Adresse', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))    
    filiere = forms.CharField(label='Filiere', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    projet = forms.CharField(label='Projet', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))    
    filename = forms.CharField(label='CV', max_length=200, widget=forms.FileInput(attrs={'class':'form-control login-input'}))

