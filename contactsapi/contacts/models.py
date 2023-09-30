from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    country_code = models.IntegerField()
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact_picture = models.URLField(null=True)
    is_favourite = models.BooleanField(default=False)
