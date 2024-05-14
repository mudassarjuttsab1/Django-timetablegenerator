from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    department = models.ForeignKey(Department,null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    
    department = models.ForeignKey(Department,null=False, on_delete=models.CASCADE)

    teachers = models.ManyToManyField(Teacher)
    
    def __str__(self):
        return self.name
    
# class TeacherCourse(models.Model):
#     teacher_id = models.ForeignKey(Teacher,null=False, on_delete=models.CASCADE)

#     course_id = models.ForeignKey(Course,null=False, on_delete=models.CASCADE)