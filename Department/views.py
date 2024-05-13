from django.shortcuts import render,redirect
from django.views.generic import TemplateView

from . import forms
from .models import Department,Teacher
# Create your views here.


class DepartmentView(TemplateView):
     template_name = 'department/new_department.html'

     def get(self,request):
        form = forms.DepartmentForm()
        return render(request,'department/new_department.html',{'form': form})

     def post(self,request):
         message = ''

         if request.method == 'POST':
             form = forms.DepartmentForm(request.POST)

             if form.is_valid():
                 form.save()
                 message = f"Department is successfully created"
                 print(message)
                 return redirect('/department_new')
         return render(request,'department/new_department.html',{'form': form})
class DepartmentListView(TemplateView):
     template_name = 'index.html'


     def get(self,request):
         departments = Department.objects.all()
         print(departments)
         return render(request,'department/index.html',{'departments': departments})


class TeacherView(TemplateView):

    def get(self,request):
        template_name = 'Teacher/new_teacher.html'
        departments = Department.objects.all()
        form = forms.TeacherForm()
        return render(request,template_name,{'form': form,'departments': departments})
    
    def post(self,request):
        template_name = 'Teacher/new_teacher.html'

        message = ''

        if request.method == 'POST':
            breakpoint()
            form = forms.TeacherForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('/departments')
            

        return render(request,template_name,{'form': form})

