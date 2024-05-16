from django.urls import path
from Department import views
urlpatterns = [
    path('department/',views.DepartmentView.as_view(),name='department'),
    path('department/<int:id>/', views.DepartmentShowView.as_view(),name='department_show'),
    path('departments/',views.DepartmentListView.as_view(),name='department_index'),
    path('teacher/',views.TeacherView.as_view(),name="teacher"),
    path('teachers/', views.TeacherListView.as_view(), name="teachers"),
    path('department/<int:department_id>/add_course/',views.CourseView.as_view(),name="course"),
    path('department/<int:department_id>/courses',views.CourseListView.as_view(),name='courses'),
    path('ajax/load-teachers/', views.load_teachers, name='load_teachers'),
]
