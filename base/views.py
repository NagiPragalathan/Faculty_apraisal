from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/Admin/')
def home(request):
    return render(request,"dashboard/dashboard.html")

def tables(request):
    return render(request,"dashboard/tables.html")

def profile(request):
    return render(request,"dashboard/profile.html")

def billing(request):
    return render(request,"dashboard/billing.html")



@login_required()
def staff_home(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    return render(request,"home/home_page.html",{'user_name':usr_obj.username})

def login_page(request):
    return render(request,"sample/login.html")

def login_into_home(request):
    user_name = request.POST.get('usr_name')
    password = request.POST.get('password')
    print(user_name,password)
    user = authenticate(username=user_name, password=password)
    print(user)
    if user is not None:
        login(request, user)
        user_detials = Users.objects.get(user_name = user_name)
        role = user_detials.role
        usr_name = user_detials.user_name
        if role == 3 :
            return redirect('/staff_home')
        elif role == 2:
            return redirect('/staff_home')
        elif role == 1:
            return redirect('Admin/Admin_home')
    else:
        return render(request,"sample/login.html")
    

def add_staff_hod(request):
    return render(request,"sample/Admin_add_staff.html")

def add_usr(request):
    usr_name = request.POST.get('user_name')
    password = request.POST.get('password')
    role = request.POST.get('roles')
    mail = request.POST.get('mail')
    try :
        add_user = Users(user_name=usr_name,mail_id=mail,password=password,role=role)
        add_user.save()
        user = User.objects.create_user(usr_name, mail, password)
        user.save()
    except:
        print("The value already exist....")
    return render(request,"dashboard/tables.html")

