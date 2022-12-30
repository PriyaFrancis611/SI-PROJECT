from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth
from .models import Profile
import random


# Create your views here.
def index(request):
    return render(request, 'index.html')
def index_reg(request):
    return render(request, 'index_reg.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def index_admin(request):
    return render(request, 'index_admin.html')
def profile_edit(request):
    return render(request,'profile_edit.html')
def profile(request):
    return render(request,'profile.html')
def dashboard(request):
    user = request.user
    user_data = User.objects.filter(id=user.id)
    print(user_data)
    print(user.id)
    Profile_data = Profile.objects.filter(user_id=user.id)
    print(Profile_data)
    # user_id = request.session['user_id']
    # print(user_id)
    # userDetails =
    return render(request, 'dashboard.html', {"userDetails": user, "profiledata": Profile_data})

def profile_edit(request):
    user = request.user
    user_data = User.objects.filter(id=user.id)
    print(user_data)
    print(user.id)
    Profile_data = Profile.objects.filter(user_id=user.id)
    print(Profile_data)
    return render(request, 'profile_edit.html', {"userDetails": user, "profiledata": Profile_data})

def profile(request):
    user = request.user
    user_data = User.objects.filter(id=user.id)
    print(user_data)
    print(user.id)
    Profile_data = Profile.objects.filter(user_id=user.id)
    print(Profile_data)
    # user_id = request.session['user_id']
    # print(user_id)
    # userDetails =
    return render(request, 'profile.html', {"userDetails": user, "profiledata": Profile_data})





def courses(request):
    return render(request, 'courses.html')


# def signup(request):
#     if request.method=="POST":
#         form=Registration(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             if form.cleaned_data['password']==form.cleaned_data['confirm_password']:
#                 if User.objects.filter(email=form.cleaned_data['email']).exists():
#                     print("Email already exists")
#                     return redirect('signup')
#                 else:
#                     user=User.objects.create_user(username=form.cleaned_data['username'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],email=form.cleaned_data['email'],password=form.cleaned_data['password'])
#                     user.save()
#                     profile=Profile(user=user,gender=form.cleaned_data['gender'],phone_number=form.cleaned_data['phone_number'],country=form.cleaned_data['country'],state=form.cleaned_data['state'],city=form.cleaned_data['city'])
#                     profile.save()
#                     return redirect('signup')
#             else:
#                  print('password mismatch')
#                  return redirect('signup')

#         else:
#             print('form incomplete')
#             return redirect('signup')
#     else:
#         form=Registration()
#         return render(request,'index_reg.html',{'form':form})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if (password == confirm_password):
            if User.objects.filter(username=username).exists():
                print('username exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                print('email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.first_name = first_name
                user.last_name = last_name

                subject = 'Welcome to Scope India'
                message = f'Hi {user.username}, thank you for registering in scope india.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)

                print('user created')
                user.save()
                details = Profile()
                details.user = user
                details.gender = request.POST['gender']
                details.contact_no = request.POST['contact_no']
                details.country = request.POST['country']
                details.state = request.POST['state']
                details.city = request.POST['city']

                details.save()
                return HttpResponse("successfully saved")
        else:
            print('password not matching..')
            return redirect('signup')
    else:
        return render(request, 'index_reg.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        Login_password = request.POST['password']
        # print(Login_password)
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            # print(User.check_password(Login_password))
            userlogin = authenticate(request, username=username, password=Login_password)
            # print(userlogin)
            if userlogin is not None:
                if user:
                    auth.login(request, user)
                    # request.session['user_id'] = user.user_id
                    request.session['user_status'] = 'logged in'
                    return redirect('dashboard')
            else:
                return render(request, 'Login.html')
        else:
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')


def logout(request):
    auth.logout(request)
    request.session['user_status'] = 'logged out'
    return redirect(index)

# def search(request):
#     if request.method=='POST':
#         courses_list=request.POST.getlist('search')

def change_password(request):
    if request.method=="POST":
        existing_password=request.POST['Existing Password']
        new_password=request.POST['New Password']
        if(existing_password==new_password):
            print('password changed successfully')
            return redirect('login')
        else:
            print('password is not matching...')
            return redirect('change_password')
    else:
        return render(request,'change_password.html')

# class SearchView(ListView):
#     model= Courses
#     template_name= "courses.html"
#     context_object_name="posts"

# def forgot_password(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         email=request.POST['email']
#         if User.objects.filter(username=username).exists():
#             user = User.objects.get(username=username)
#             subject = 'Welcome to Scope India'
#             message = f'Hi {user.username}, your password is .'
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [user.email, ]
#             send_mail(subject, message, email_from, recipient_list)
#         else:
#             print('username exists')
#             return redirect('forgot_password')
#     else:
#         return render(request,'forgot_password.html')


# def forgot_password(request):
#     if request.method == 'POST':
#         return render(request, from_email=request.POST.get('email'))
#     else:
#         return render(request, 'forgot_password.html')

# def forgot_password(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         if User.objects.filter(username=username).exists():
#             return redirect('forgot_password')
#         else:
#             return render(request,'forgot_password.html')
#         user_obj=User.objects.get(username=username)
#         token=str(random.randrange(100000,1000000))
#         subject='your forget password link'
#         message=f'Hi,click on the link to reset your password http://127.0.0.1:8000/change_password'
#         email_from=settings.EMAIL_HOST_USER
#         recipient_list=[email]
#         send_mail(subject,message,email_from,recipient_list)
#         return redirect('forgot_password')
#     else:
#         return render(request,'forgot_password.html')

def forgot_password(request):
    if request.method=="POST":
        username=request.POST['username']
        user=User.objects.get(username=username)
        profile=Profile.objects.get(user=user)
        user_email=user.email
        token=profile.forget_token
        message=f'Hi,click on the link to reset your password http://127.0.0.1:8000/change_password'
        send_mail('password reset request',message,settings.EMAIL_HOST_USER,[user_email],fail_silently=False)

    return render(request,'forgot_password.html')
