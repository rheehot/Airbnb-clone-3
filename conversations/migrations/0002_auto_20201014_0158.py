# Generated by Django 2.2.5 on 2020-10-13 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='uesr',
            new_name='user',
        ),
    ]
