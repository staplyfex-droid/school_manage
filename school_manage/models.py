from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)

class Schedule(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()