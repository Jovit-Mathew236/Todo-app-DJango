# Generated by Django 4.1.4 on 2023-01-17 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todopro', '0003_todos_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todos',
            name='day',
        ),
    ]
