# Generated by Django 4.0.5 on 2022-07-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_alter_auteur_name_alter_auteur_prenom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='auteur',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myblog.auteur'),
        ),
    ]