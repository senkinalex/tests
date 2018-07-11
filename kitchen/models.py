from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class MenuItem(models.Model):
    item = models.TextField()
    price = models.DecimalField(decimal_places=2)
    weight = models.SmallIntegerField()
    pub_date = models.DateTimeField('date published')


class Menu(models.Model):
    blob = models.ForeignKey(MenuItem, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    lock_key = models.SmallIntegerField(unique_for_date=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False, primary_key=True)
    about_user = models.CharField(blank=True, default='')

# class Orders(models.Model):
# #     order = pass
