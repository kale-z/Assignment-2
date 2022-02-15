from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    office = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField()

class Course(models.Model):
    name = models.CharField(max_length=30)
    classroom = models.CharField(max_length=50)
    code = models.CharField(max_length=60)
    time = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)