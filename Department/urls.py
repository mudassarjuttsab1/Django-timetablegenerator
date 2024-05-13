from django.urls import path
from Department import views
urlpatterns = [
    path('department/',views.DepartmentView.as_view(),name='department'),
    path('departments/',views.DepartmentListView.as_view(),name='department_index'),
    path('teacher/',views.TeacherView.as_view(),name="teacher")
]
