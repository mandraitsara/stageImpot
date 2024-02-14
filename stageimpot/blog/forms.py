from django import forms

class loginStageForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, widget=forms.TextInput(attrs={'class':'form-control login-input'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control login-input'}))
