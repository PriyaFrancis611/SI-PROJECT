from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('index_reg/',views.index_reg,name='index_reg'),
    path('login/',views.login,name='login'),
    path('registration/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('index_admin/',views.index_admin,name='index_admin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('courses/',views.courses,name='courses'),
    path('logout/',views.logout,name='logout'),
    # path('profile_edit/<int:id>',views.profile_edit,name='profile_edit'),
    path('profile_edit/',views.profile_edit,name='profile_edit'),
    path('profile/',views.profile,name='profile'),
    path('change_password/<str:token>',views.change_password,name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    # path("reset-password/<String:token>",views.resetpassword,name="")
    path('password/',views.password,name='password'),
    path('search/',views.search,name='search'),
    path('services/',views.services,name='services')

]