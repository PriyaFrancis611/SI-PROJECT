from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Forgot_token(models.Model):
    token = models.CharField(max_length=200)
    user_id = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # forget_token=models.CharField(max_length=1000)
    contact_no = models.IntegerField()
    date_of_birth = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    hobbies=models.CharField(max_length=200)
    upload_avatar=models.FileField(upload_to='documents')
    # avatar = models.ImageField(upload_to='images')
    # username=models.CharField(max_length=30)
    # first_name=models.CharField(max_length=30)
    # last_name=models.CharField(max_length=30)
    # gender=models.CharField(max_length=30)
    # date_of_birth=models.CharField(max_length=30)
    # email=models.EmailField()
    # phone_number=models.IntegerField()
    # country=models.CharField(max_length=30)
    # state=models.CharField(max_length=30)
    # city=models.CharField(max_length=30)

    # password=models.CharField(max_length=30)
    # confirm_password=models.CharField(max_length=30)


class Courses(models.Model):
    title=models.CharField(max_length=150)
    # created_at=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=550)

#     def __str__(self):
#         return self.title
