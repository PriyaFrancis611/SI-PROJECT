from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'index.html')


def index_reg(request):
    return render(request, 'index_reg.html')


# def login(request):
#     return render(request,'login.html')
def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index_admin(request):
    return render(request, 'index_admin.html')


def dashboard(request):
    user = request.user
    user_data = User.objects.filter(id=user.id)
    print(user_data)
    Profile_data = Profile.objects.filter(id=user.id)
    print(Profile_data)
    # for i in Profile_data:
    #     print(i)
    # user_id = request.session['user_id']
    # print(user_id)
    # userDetails =
    return render(request, 'dashboard.html', {"userDetails": user, "profiledata": Profile_data})


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

        # else:
        #     addrec_path = 'index_reg.html'
        #     return render(request, addrec_path)

    # def login(request):
    #     if request.method == "POST":
    #         username = request.POST['fullname']
    #         email=request.POST['email']
    #         Login_password = request.POST['password']
    #         print(Login_password)
    #         if User.objects.filter(username=username).exists():
    #             user = User.objects.get(username=username)
    #             print(user)
    #             # print(User.check_password(Login_password))
    #             userlogin = authenticate(request, username=username,email=email, password=Login_password)
    #             print(userlogin)
    #             if userlogin is not None:
    #                 if user:
    #                     auth.login(request, user)
    #                     request.session['user_status'] = 'logged in'
    #                     return redirect('index')
    #             else:
    #                 return render(request, 'Login.html')
    #         else:
    #             return render(request, 'Login.html')
    #     else:
    #         return render(request, 'Login.html')


# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password=request.POST['password']
#         user=auth.authenticate(request,username=username,email=email,password=password)
#     if user is not None:
#         login(request,user)
#         return redirect('index')
#     else:
#         print("There was an error logging in,try again...")
#         return redirect('login')
#     else:
#         return render(request,'login.html')
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
#