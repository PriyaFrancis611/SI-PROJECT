# Generated by Django 4.1.2 on 2022-12-15 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SI', '0006_remove_profile_user_id_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_id',
        ),
    ]
