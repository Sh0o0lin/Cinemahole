from django.db import models
from django.contrib.postgres.fields import ArrayField


class Person(models.Model):
    gender_choices=(
        ('male','Male'),
        ('female','Female'),
        ('unknown','Unknown'),
        ('non-binary','Non-Binary'))
    birthday=models.DateField(null=True)
    aka=ArrayField(models.CharField(max_length=250,blank=True),size=20,blank=True)
    known_for_department=models.CharField(max_length=200,null=True)
    deathday=models.DateField(null=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(choices=gender_choices,max_length=10)
    biography=models.TextField(null=True)
    popularity=models.DecimalField(max_digits=20,decimal_places=10)
    birth_place=models.CharField(max_length=200,null=True)
    imdb_id=models.CharField(max_length=50,null=True)
    homepage=models.CharField(max_length=250,null=True)