# Generated by Django 5.0.2 on 2024-03-05 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='demandeStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lettre_de_motivation', models.CharField(max_length=500)),
                ('projet', models.CharField(max_length=200)),
                ('fichier', models.ImageField(upload_to='media')),
                ('dates', models.DateTimeField(auto_now=True)),
                ('observation', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=10)),
                ('departement', models.CharField(max_length=150)),
                ('lieux_de_stage', models.CharField(max_length=150)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='notificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projet', models.CharField(max_length=200)),
                ('notification', models.CharField(max_length=200)),
                ('obs', models.BooleanField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userCompleteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_de_naissance', models.DateField(max_length=200)),
                ('filiere', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('ecole', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]