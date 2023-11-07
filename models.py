from django.db import models

class studentInfo(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
