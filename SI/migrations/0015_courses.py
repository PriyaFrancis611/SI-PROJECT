# Generated by Django 4.1.2 on 2023-01-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SI', '0014_rename_forgottoken_forgot_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=550)),
            ],
        ),
    ]