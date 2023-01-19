from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Users, Faculty_details, Subjects, Subject_handled, Details, IV_Details
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from faculty_apraisal.settings import BASE_DIR
import datetime
import os
from bing_image_downloader import downloader
# Create your views here.

@login_required(login_url='/Admin/')
def home(request):
    return render(request,"dashboard/dashboard.html")

def tables(request):
    facultys = Faculty_details.objects.all()
    for i in facultys:
        print(i.name)
    return render(request,"dashboard/tables.html",{'users':facultys})

def profile(request):
    department = []
    sem=[]
    img = {}
    subs = Subjects.objects.all()
    for i in subs:
        if i.department not in department:
            department.append(i.department)
        if i.semester not in sem:
            sem.append(i.semester)
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(user_name=usr_obj.username)
    for i in subs:
        try:
            item = os.listdir(i.subject_image)
        except:
            item = 'hi.jpg'
            print('file not found')
        path = "static\\" + i.subject_image.split('static\\')[1] + "\\" + item[0]
        img[i.subject_code] = path
    return render(request,"dashboard/profile.html",{'detail':faculty_details,'subs':subs,"dep":department,"sem":sem,"img":img})


def billing(request):
    return render(request,"dashboard/billing.html")

@login_required()
def staff_home(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    name = Users.objects.get(user_name=usr_obj.username)
    faculty_details = Faculty_details.objects.get(user_name=name.user_name)
    return render(request,"home/home_page.html",{'user_name':usr_obj.username,'detials':faculty_details})

def login_page(request):
    return render(request,"login/login.html.j2")

def sign_out(request):
    logout()
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

def Personal_detials(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(user_name=usr_obj.username)
    # request and get datas ..............
    role = Users.objects.get(user_name = usr_obj.username)
    id_number = request.POST.get('idcard')
    name1 = request.POST.get('F_name')
    name2 = request.POST.get('surname')
    name = name1+' '+name2
    designation = request.POST.get('designation')
    department = request.POST.get('department')
    experience = request.POST.get('experience')
    qualififcation = request.POST.get('qualififcation')
    assessment_period = request.POST.get('AP')
    date_of_join = request.POST.get('date')
    bio = request.POST.get('about')
    d = date_of_join.split("-")
    date_formate = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    my_uploaded_file = request.FILES['file_upload']
    print(date_of_join)
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    edit = Faculty_details.objects.get(user_name=usr_obj.username)
    edit.role=role
    edit.id_number=id_number
    edit.designation=designation
    edit.department=department
    edit.experience=experience
    edit.qualififcation=qualififcation
    edit.assessment_period=assessment_period
    edit.date_of_join=date_formate
    edit.image = my_uploaded_file
    edit.bio=bio
    edit.save()
    return render(request,"home/home_page.html",{'user_name':usr_obj.username,'detials':faculty_details})



def add_usr(request):
    usr_name = request.POST.get('user_name')
    password = request.POST.get('mail')
    role = request.POST.get('roles')
    mail = request.POST.get('password')

    facultys = Faculty_details.objects.all()
    for i in facultys:
        print(i.name)
        
    add_user = Users(user_name=usr_name,mail_id=mail,password=password,role=role)
    add_user.save()
    current_user = Users.objects.get(user_name=usr_name)
    Fac_del = Faculty_details(user_name=usr_name,role=current_user, id_number=0, name=add_user.user_name)
    Fac_del.save()
    user = User.objects.create_user(usr_name, mail, password)
    user.save()
    return redirect(request,"dashboard/tables.html",{'users':facultys})

def view_usr(request):
    fac = Subject_handled.objects.all()
    print(len(fac))
    # Fac_del = Faculty_details(role=request.user.id, id_number=0, name=request.user.username, user_name=request.user.username)
    # Fac_del.save()
    return render(request,"sample/view.html",{'usr':fac,'path':os.path.join(os.path.join(BASE_DIR, 'static'),'image_pics')})

def add_subject(request):
    return render(request,"dashboard/Subject_updater.html")

def select_subject(request):
    department = []
    sem=[]
    img = {}
    subs = Subjects.objects.all()
    for i in subs:
        if i.department not in department:
            department.append(i.department)
        if i.semester not in sem:
            sem.append(i.semester)
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    choosed_sub = []
    faculty_details = Faculty_details.objects.get(user_name=usr_obj.username)
    for i in subs:
        try:
            item = os.listdir(i.subject_image)
        except:
            item = 'hi.jpg'
            print('file not found')
        path = "static\\" + i.subject_image.split('static\\')[1] + "\\" + item[0]
        img[i.subject_code] = path
        sub_detials = Subject_handled.objects.all()
    for i in sub_detials:
        if faculty_details.id == i.faculty_id :
            choosed_sub.append(i.subject_code)
            print(i.subject_code)
    return render(request,"staff/Add_subject.html",{'detail':faculty_details,'subs':subs,"dep":department,"sem":sem,"img":img,'choosed':choosed_sub})



def save_subject(request):
    subject_name = request.POST.get("txtName")
    subject_code = request.POST.get("subcode")
    semester     = request.POST.get("sem")
    department   = request.POST.get("dep")
    discription  = request.POST.get("dis")
    urls = str(os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'),'image_pics'),"_".join(subject_name.split(' '))))
    add_sub = Subjects(subject_image=urls,subject_name=subject_name,subject_code=subject_code,semester=semester,
                        department=department,discription=discription)
    add_sub.save()
    downloader.download("_".join(subject_name.split(' ')), limit=2, output_dir=os.path.join(os.path.join(BASE_DIR, 'static'),'image_pics'), adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
    data = Subjects.objects.all()
    for i in data:
        print(i.subject_image,i.subject_name)
    return render(request,"dashboard/Subject_updater.html")

def add_sub(request):
    department = []
    sem=[]
    img = {}
    subs = Subjects.objects.all()
    for i in subs:
        if i.department not in department:
            department.append(i.department)
        if i.semester not in sem:
            sem.append(i.semester)
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(user_name=usr_obj.username)
    for i in subs:
        try:
            item = os.listdir(i.subject_image)
        except:
            item = 'hi.jpg'
            print('file not found')
        path = "static\\" + i.subject_image.split('static\\')[1] + "\\" + item[0]
        img[i.subject_code] = path
    choosed_sub = []
    sub_code = request.GET.get('subcode')
    sub = Subjects.objects.get(subject_code=sub_code)
    subject = Subject_handled(faculty_id = faculty_details.id,subject_staff = faculty_details,subject_name=sub.subject_name,
                              subject_code = sub.subject_code ) 
    subject.save()
    sub_detials = Subject_handled.objects.all()
    for i in sub_detials:
        choosed_sub.append(i.subject_code)
        print(i.subject_code)
    return render(request,"staff/Add_subject.html",{'detail':faculty_details,'subs':subs,"dep":department,"sem":sem,"img":img,'choosed':choosed_sub})


def rm_sub(request):
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(user_name=usr_obj.username)
    sub_code = request.GET.get('subcode')
    subject = Subject_handled.objects.get(faculty_id=faculty_details.id,subject_code = sub_code )
    subject.delete()
    return render(request,"staff/Add_subject.html")

def guest_lecture(request):
    return render(request,"staff/Guest_lecture.html")

def add_guest_lecture(request):
    name = request.POST.get('user_name')
    date = request.POST.get('date')
    designation = request.POST.get('designation')
    topic = request.POST.get('topic')
    coming_from = request.POST.get('coming_from')
    mail_id = request.POST.get('email')
    image = request.FILES['image']
    d = date.split("-")
    date_formate = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    faculty_details = Faculty_details.objects.get(user_name=usr_obj.username)
    add_detial = Details(faculty_id=faculty_details.id,name=name,designation=designation,
                         topic=topic,coming_from = coming_from,mail_id=mail_id,image=image,date=date_formate)
    add_detial.save()

    details = Details.objects.all()

    return render(request,"staff/Guest_lecture.html",{'details':details})

def add_IV(request):
    name = request.POST.get('user_name')
    date = request.POST.get('date')
    place = request.POST.get('designation')
    no_of_stu = request.POST.get('topic')
    IV_detials = request.POST.get('coming_from')
    faculty_detials = request.POST.get('email')
    d = date.split("-")
    date_formate = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    usr_id = request.user.id
    usr_obj = User.objects.get(id=usr_id)
    add_IV = IV_Details(name=name,place=place,no_of_stu=no_of_stu,IV_detials=IV_detials
                        )
    add_IV.save()

    details = Details.objects.all()

    return render(request,"staff/Guest_lecture.html",{'details':details})

