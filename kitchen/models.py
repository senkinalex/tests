from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class MenuItem(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateTimeField('date entered', auto_now_add=True)


class DayMenu(models.Model):
    Monday = 'Пн'
    Tuesday = 'Вт'
    Wednesday = 'Ср'
    Thursday = 'Чт'
    Friday = 'Пт'
    Saturday = 'Сб'
    Sunday = 'Вс'
    WEEK_DAY_CHOICES = (
        (Monday, 'Понедельник'),
        (Tuesday, 'Вторник'),
        (Wednesday, 'Среда'),
        (Thursday, 'Четверг'),
        (Friday, 'Пятница'),
        (Saturday, 'Суббота'),
        (Sunday, 'Воскресенье'),
    )

    blob = models.ForeignKey(MenuItem, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    created = models.DateTimeField('date published', auto_now_add=True)


class WeekMenu(models.Model):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False, primary_key=True)
    about_user = models.CharField(blank=True, default='')

# class Orders(models.Model):
# #     order = pass
