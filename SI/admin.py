from django.contrib import admin

# Register your models here.
from . models import Country,State,City,Profile,Courses
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Courses)