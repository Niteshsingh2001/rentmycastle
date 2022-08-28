from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    img1 = models.ImageField(upload_to='uploads/', default="")
    img2 = models.ImageField(upload_to='uploads/', default="")
    img3 = models.ImageField(upload_to='uploads/', default="")
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    posted_by = models.CharField(max_length=100)
    post_date = models.DateField()
    price = models.IntegerField()
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class users_data(models.Model):
    username = models.CharField(max_length=100)
    # phone_no = models.IntegerField()
    # profile = models.ImageField(upload_to="profile")
