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
                 return redirect('/departments')
         return render(request,'department/new_department.html',{'form': form})
class DepartmentListView(TemplateView):
     template_name = 'index.html'


     def get(self,request):
         departments = Department.objects.all()
         print(departments)
         return render(request,'department/index.html',{'departments': departments})


class TeacherView(TemplateView):
    template_name = 'teacher/new_teacher.html'

    def get(self,request):
        departments = Department.objects.all()
        form = forms.TeacherForm()
        return render(request,self.template_name,{'form': form,'departments': departments})
    
    def post(self,request):
        message = ''
        if request.method == 'POST':
            form = forms.TeacherForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('/teachers')

        return render(request,self.template_name,{'form': form})

class TeacherListView(TemplateView):
    template_name = "teacher/index.html"
    def get(self,request):
        teachers = Teacher.objects.all()
        return render(request,self.template_name,{'teachers': teachers})
    

class CourseView(TemplateView):
    template_name = 'course/new_course.html'

    def get(self,request):
        departments = Department.objects.all()
        form = forms.CourseForm()
        return render(request,self.template_name,{'form': form})
    
    def post(self,request):
        breakpoint()