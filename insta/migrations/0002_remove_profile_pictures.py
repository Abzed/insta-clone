# Generated by Django 3.1.2 on 2020-10-19 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pictures',
        ),
    ]
