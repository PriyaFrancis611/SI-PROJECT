# Generated by Django 4.1.2 on 2023-01-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SI', '0009_rename_phone_number_profile_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.CharField(default='exit', max_length=30),
            preserve_default=False,
        ),
    ]
