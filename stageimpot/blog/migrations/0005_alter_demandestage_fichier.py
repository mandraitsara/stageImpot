# Generated by Django 5.0.2 on 2024-03-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_demandestage_fichier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandestage',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]