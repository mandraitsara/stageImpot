# Generated by Django 5.0.2 on 2024-03-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_directionuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandestage',
            name='fichier',
            field=models.FileField(default='inconnu.png', upload_to=''),
        ),
    ]
