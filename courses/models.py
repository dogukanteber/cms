from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Course(models.Model):
    DANCE = "Dance"
    PROG = "Programming"
    LANG = "Language"
    TYPES = [
        (DANCE, "Dance"),
        (PROG, "Programming"),
        (LANG, "Language"),
    ]
    name = models.CharField(max_length=100)
    desc = models.TextField()
    type = models.CharField(max_length=15, choices=TYPES, default=DANCE)
    due_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def is_past_due(self):
        return timezone.now() > self.due_date


class UserDetail(models.Model):
    telephone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=512)
    profession = models.CharField(max_length=64)

    def __str__(self):
        return self.profession