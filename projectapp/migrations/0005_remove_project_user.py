# Generated by Django 4.2.4 on 2023-09-13 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
    ]
