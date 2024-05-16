from .models import Department,Teacher,Course
from . import models
from django import forms

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name']


class TeacherForm(forms.ModelForm):


    class Meta:
        model = Teacher

        fields = ['name','department']


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = ['name', 'teacher']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['teacher'].queryset = Teacher.objects.none()
    #     if 'department' in self.data:
    #         try:
    #             department_id = int(self.data.get('department'))
    #             self.fields['teacher'].queryset = Teacher.objects.filter(department_id=department_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # Invalid input from the client; ignore and fallback to empty Teacher queryset
    #     elif self.instance.pk:
    #         self.fields['teacher'].queryset = self.instance.department.teacher_set.all().order_by('name')
