from .models import Department,Teacher

from django import forms

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name']


class TeacherForm(forms.Form):

        name = forms.CharField(label='Teacher Name')
        department_id = forms.ModelChoiceField(queryset=Department.objects.all(), label='Department')