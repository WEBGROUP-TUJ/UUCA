from django.db import models
from django.contrib.auth.models import AbstractUser

DEGREES = (
    (u'B', u'Bachelor'),
    (u'M', u'Master'),
    (u'D', u'Doctor'),
)


class CustomUser(AbstractUser):
    pass


class UserSettings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    degree = models.CharField(max_length=20, choices=DEGREES)

    def __str__(self):
        return self.user.username