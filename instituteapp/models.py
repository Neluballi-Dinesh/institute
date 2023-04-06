from django.db import models


class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    start_date=models.DateField(max_length=100)
    fee=models.IntegerField()
    timings=models.CharField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.CharField(max_length=100)


class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=100)
    location=models.CharField(max_length=100)


class feedbackData(models.Model):
    content=models.TextField(max_length=1000)
    date=models.DateField(max_length=100)
