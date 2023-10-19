from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=50)
    pass_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

