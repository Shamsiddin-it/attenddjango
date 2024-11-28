from django.db import models
from django.contrib.auth.models import User
    
class Teacher(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField( max_length=50)
    time = models.TimeField()
    price = models.DecimalField( max_digits=6, decimal_places=2)
    description = models.TextField()
    max_students = models.IntegerField()
    min_students = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)
    start = models.DateField( auto_now=False, auto_now_add=False)
    end = models.DateField( auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=250)
    course = models.ManyToManyField(Course)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    STATUS = (
        ('came', 'came'),
        ('late', 'late'),
        ('absent', 'absent'),
        ('left', 'left')
    )
    reason = models.CharField( max_length=250, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=50)
    time = models.DateTimeField( auto_now=True)
    def __str__(self):
        return self.student
    