from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('index_reg/',views.index_reg,name='index_reg'),
    path('login/',views.login,name='login'),
    path('registration/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')
    # path('addrec/',views.addrec,name='addrec')
]