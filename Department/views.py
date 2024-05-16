from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView

from . import forms
from .models import Department,Teacher
from . import models
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

class DepartmentShowView(TemplateView):

    def get(self,request,id):
        department = get_object_or_404(Department,id=id)
        return render(request,'department/show.html',{'department': department})
    

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

    def get(self,request,department_id):
        department = Department.objects.get(id=department_id)
        teachers = Teacher.objects.filter(department_id=department_id)
        form = forms.CourseForm(initial={'department': department_id})
        context ={'department': department, 'teachers': teachers, 'form': form}
        return render(request,self.template_name,context)
    
    def post(self, request, department_id):
        department = get_object_or_404(Department, id=department_id)
        teachers = Teacher.objects.filter(department_id=department_id)
        form = forms.CourseForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)
            course.department = department
            course.save()
            form.save_m2m()  # Save many-to-many relationships

            return redirect('courses', department_id=department_id)  # Redirect after successful form submission
        else:
            print(form.errors)  # Print form errors to console for debugging

        context = {'department': department, 'teachers': teachers, 'form': form}
        return render(request, self.template_name, context)

class CourseListView(TeacherView):
    template_name = 'course/index.html'
    def get(self,request,department_id):

        courses = models.Course.objects.filter(department_id=department_id)
        context = {'courses': courses,'department_id': department_id}
        return render(request,self.template_name,context)
def load_teachers(request):
    breakpoint()
    department_id = request.GET.get('department_id')
    teachers = Teacher.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'course/load_teachers.html', {'teachers': teachers})