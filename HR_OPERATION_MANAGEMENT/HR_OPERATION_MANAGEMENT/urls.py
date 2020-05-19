"""HR_OPERATION_MANAGEMENT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="home_page.html"),name="home"),
    path('admin_login/',views.AdminLogin.as_view(),name='admin_login'),
    path('admin_home',TemplateView.as_view(template_name="admin_home.html"),name="admin_home"),
    path('add/',views.AddEmployee.as_view(),name='add'),
    path('view/',views.ViewEmployee.as_view(),name="view"),
    path('upadat_view/',views.Upadatview.as_view(),name="upadat_view"),
    path('update_employee/<int:pk>',views.UpdateEemployee.as_view(),name="update_employee"),
    path('del_page/',views.DelPage.as_view(),name="del_page"),
    path('del_emp/',views.DeleteEmployee.as_view(),name='del_emp'),
]
