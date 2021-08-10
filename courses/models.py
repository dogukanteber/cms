from django.db import models

class Course(models.Model):
    DANCE = "Dance"
    PROG = "Programming"
    LANG = "Language"
    TYPES = [
        (DANCE, "Dance"),
        (PROG, "Programming"),
        (LANG, "Language"),
    ]
    name = models.CharField(max_length=20)
    desc = models.TextField()
    type = models.CharField(max_length=15, choices=TYPES, default=DANCE)
    due_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name