# Generated by Django 5.0.6 on 2024-05-08 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_lastname_user_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastname',
        ),
    ]