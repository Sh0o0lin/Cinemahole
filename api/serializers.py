import ast
import json
from rest_framework import serializers
from person.models import Person
from movie.models import Movie,Credit,Keyword,Cast,Crew
from miscellany.models import Genre,Language,ProductionCompany,ProductionCountry


class GenreSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.name
    class Meta:
        model=Genre

class KeywordSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.name
    class Meta:
        model=Keyword

class ProductionCompanySerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.name
    class Meta:
        model=ProductionCompany

class ProductionCountrySerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.iso_3166_1
    class Meta:
        model=ProductionCountry

class LanguageSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
         return value.name
    class Meta:
        model=Language

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cast
        fields='__all__'

class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crew
        fields='__all__'

class CreditSerializer(serializers.ModelSerializer):
    cast=CastSerializer(read_only=True,many=True)
    crew=CrewSerializer(read_only=True,many=True)
    class Meta:
        model=Credit
        fields='__all__'
        
class MovieDetailSerializer(serializers.ModelSerializer):
    genres=GenreSerializer(read_only=True,many=True)
    keywords=KeywordSerializer(read_only=True,many=True)
    production_companies=ProductionCompanySerializer(read_only=True,many=True)
    production_countries=ProductionCountrySerializer(read_only=True,many=True)
    original_language=LanguageSerializer(read_only=True)
    spoken_languages=LanguageSerializer(read_only=True,many=True)
    credit=CreditSerializer(read_only=True)
    class Meta:
        model=Movie
        fields='__all__'
