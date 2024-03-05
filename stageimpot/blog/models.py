from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class demandeStage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lettre_de_motivation = models.CharField(max_length=500)
    projet = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='media', null=True , blank=True)
    dates = models.DateTimeField(auto_now=True)
    observation = models.CharField(max_length=200)
    note = models.CharField(max_length=10)
    departement = models.CharField(max_length=150)
    lieux_de_stage = models.CharField(max_length=150)
    


class userCompleteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_de_naissance = models.DateField(max_length=200)
    filiere = models.CharField(max_length=200)    
    telephone = models.CharField(max_length=200)
    ecole = models.CharField(max_length=200)

class notificationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    projet = models.CharField(max_length=200)
    notification = models.CharField(max_length=200)
    obs = models.BooleanField()

class directionUser(models.Model):
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=100)