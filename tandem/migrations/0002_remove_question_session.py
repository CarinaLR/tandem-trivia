# Generated by Django 3.1.2 on 2020-10-29 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tandem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='session',
        ),
    ]
