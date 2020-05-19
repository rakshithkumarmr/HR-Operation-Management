from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView
from app.models import Employee
from django.contrib.messages.views import SuccessMessageMixin

class AdminLogin(View):
    def get(self,request):
        return render(request,"admin_login.html")
    def post(self,request):
        username=request.POST['u1']
        password=request.POST['p1']
        if username=='admin' and password=='admin':
            return render(request,"admin_home.html")
        else:
            messages.success(request,'Invalid User Details')
            return redirect('admin_login')


class AddEmployee(SuccessMessageMixin,CreateView):
    model = Employee
    template_name ="add_employee.html"
    success_url = "/add/"
    fields = "__all__"
    success_message = "Employee Successfully saved"


class ViewEmployee(ListView):
    model = Employee
    template_name = "view_employee.html"


class Upadatview(ListView):
    model = Employee
    template_name = "updateview.html"


class UpdateEemployee(SuccessMessageMixin,UpdateView):
    model = Employee
    template_name = "update_employee.html"
    success_url = "/upadat_view/"
    fields = "__all__"
    success_message = "Employee Successfully updated"


class DelPage(ListView):
    model = Employee
    template_name = "del_page.html"
    fields="__all__"


class DeleteEmployee(View):
    def post(self,request):
        de=request.POST.getlist('del')
        for x in de:
            Employee.objects.get(id=x).delete()
        messages.success(request,"Employee's Successfully Deleted")
        return redirect('del_page')