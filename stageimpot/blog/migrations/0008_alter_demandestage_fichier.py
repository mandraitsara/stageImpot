# Generated by Django 5.0.2 on 2024-03-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_demandestage_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandestage',
            name='fichier',
            field=models.FileField(upload_to=''),
        ),
    ]
