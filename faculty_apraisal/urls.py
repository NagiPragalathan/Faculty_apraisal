"""faculty_apraisal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = []     

def Path_manager(Paths):
    Stack_Path = []
    for i in Paths:
        for j in i:
            Stack_Path.append(j)
    return Stack_Path

admin_path = [
    path('admin/', admin.site.urls),
    path('Admin/Admin_home/',views.home),
    path('Admin/profile/',views.profile),
    path('Admin/billing/',views.billing),
    path('Admin/tables/',views.tables),
]

admin_actions = [
    path('add_staff',views.add_staff_hod),
    path('Admin/tables/add_usr',views.add_usr)
]

home = [
    path('staff_home',views.staff_home)
]

login_path = [
    path('',views.login_page),
    path('login_to_home',views.login_into_home),
]


urlpatterns = Path_manager([admin_path,login_path,admin_actions,home])
