from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from . models import Profile


# Create your views here.
def index(request):
    return render(request,'index.html')
def index_reg(request):
    return render(request,'index_reg.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

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
    if request.method=="POST":
        username=request.POST['username']
        # firstname=request.POST['firstname']
        # lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if (password == confirm_password):
            if User.objects.filter(username=username).exists():
                print('username exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                print('email already exists')
                return redirect('signup')
            else:
               user = User.objects.create_user(username=username, password=password, email=email)
               user.save()
               print('user created')

               details = Profile()
               details.user = user
               details.gender = request.POST['gender']
               details.phonenumber = request.POST['phonenumber']
               details.country = request.POST['country']
               details.state=request.POST['state']
               details.city=request.POST['city']
               details.save()
               return HttpResponse("successfully saved")
        else:
            print('password not matching..')
            return redirect('signup')
    else:
        return render(request,'index_reg.html')

        # else:
        #     addrec_path = 'index_reg.html'
        #     return render(request, addrec_path)

    # def login(request):
    #     if request.method == "POST":
    #         username = request.POST['fullname']
    #         Login_password = request.POST['password']
    #         print(Login_password)
    #         if User.objects.filter(username=username).exists():
    #             user = User.objects.get(username=username)
    #             print(user)
    #             # print(User.check_password(Login_password))
    #             userlogin = authenticate(request, username=username, password=Login_password)
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
    #

