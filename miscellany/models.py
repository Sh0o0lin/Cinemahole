from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=50)

class Keyword(models.Model):
    name=models.CharField(max_length=50)

class Language(models.Model):
    name=models.CharField(max_length=30)
    native_name=models.CharField(max_length=30,null=True)
    code=models.CharField(max_length=20)

class ProductionCompany(models.Model):
    name=models.CharField(max_length=150)

class ProductionCountry(models.Model):
    name=models.CharField(max_length=50)
    iso_3166_1=models.CharField(max_length=20)