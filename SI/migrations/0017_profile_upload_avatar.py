# Generated by Django 4.1.2 on 2023-01-18 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SI', '0016_profile_hobbies'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='upload_avatar',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
    ]
