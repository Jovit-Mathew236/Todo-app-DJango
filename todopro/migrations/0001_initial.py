# Generated by Django 4.1.4 on 2023-01-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.TextField()),
                ('time', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
