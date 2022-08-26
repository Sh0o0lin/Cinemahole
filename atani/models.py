from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Ainur=1
    Valar=2
    Maiar=3
    ROLE_CHOICES=(
        (Ainur,'Ainur'),
        (Valar,'Valar'),
        (Maiar,'Maiar'),
    )
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=3)