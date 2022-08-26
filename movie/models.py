from django.db import models
from miscellany.models import Genre,Keyword,Language,ProductionCompany,ProductionCountry
from person.models import Person
from django.contrib.postgres.fields import ArrayField
    

class Cast(models.Model):
    gender_choices=(
        ('male','Male'),
        ('female','Female'),
        ('unknown','unknown'),
        ('non-binary','Non-Binary'))
    known_for_department=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=100)
    original_name=models.CharField(max_length=300)
    popularity=models.DecimalField(max_digits=20,decimal_places=10)
    played_by=models.ForeignKey(Person,on_delete=models.DO_NOTHING)
    character=models.CharField(max_length=600,null=True)
    gender=models.CharField(choices=gender_choices,max_length=10)
    order=models.DecimalField(max_digits=20,decimal_places=0)

class Crew(models.Model):
    gender_choices=(
        ('male','Male'),
        ('female','Female'),
        ('unknown','unknown'),
        ('non-binary','Non-Binary'))
    gender=models.CharField(choices=gender_choices,max_length=10)
    person_id=models.ForeignKey(Person,on_delete=models.DO_NOTHING)
    known_for_department=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200)
    original_name=models.CharField(max_length=500)
    popularity=models.DecimalField(max_digits=20,decimal_places=10)
    department=models.CharField(max_length=200)
    job=models.CharField(max_length=500)

class Credit(models.Model):
    cast=models.ManyToManyField(Cast)
    crew=models.ManyToManyField(Crew)

def imagefield_default():
    return {"posters":[],"backdrops":[]}

class Movie(models.Model):
    title=models.CharField(max_length=300)
    images=models.JSONField(default=imagefield_default)
    posters=models.JSONField(default=list)
    backdrops=models.JSONField(default=list)
    budget=models.DecimalField(max_digits=19,decimal_places=5)
    genres=models.ManyToManyField(Genre)
    imdb_id=models.CharField(max_length=50,null=True)
    homepage=models.CharField(max_length=650,null=True)
    keywords=models.ManyToManyField(Keyword)
    original_language=models.ForeignKey(Language,on_delete=models.DO_NOTHING)
    overview=models.TextField(null=True)
    popularity=models.DecimalField(max_digits=20,decimal_places=10)
    production_companies=models.ManyToManyField(ProductionCompany)
    production_countries=models.ManyToManyField(ProductionCountry)
    release_date=models.DateField(null=True)
    revenue=models.DecimalField(max_digits=20,decimal_places=10)
    runtime=models.DecimalField(max_digits=10,decimal_places=5,null=True)
    spoken_languages=models.ManyToManyField(Language,related_name='spoken_languages')
    status=models.CharField(max_length=50)
    tagline=models.CharField(max_length=300,null=True)
    original_title=models.CharField(max_length=250)
    vote_average=models.DecimalField(max_digits=10,decimal_places=5)
    vote_count=models.DecimalField(max_digits=10,decimal_places=0)
    credit=models.ForeignKey(Credit,on_delete=models.DO_NOTHING)
    similar_movies=ArrayField(models.DecimalField(max_digits=10,decimal_places=0))