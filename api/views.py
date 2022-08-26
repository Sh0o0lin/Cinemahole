import imp
from re import search
from django.shortcuts import get_object_or_404
from movie.models import Movie,Cast
from person.models import Person
from .serializers import MovieDetailSerializer,PersonSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import numpy as np


#MovieDetails
class MovieDetailView(APIView):
    def get(self,request,pk):
        movie=get_object_or_404(Movie,id=pk)
        serializer=MovieDetailSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)

#PopularMovies
class PopularMovies(APIView):
    def get(self,request):
        """
        votes=[float(i) for i in Movie.objects.values_list('vote_average',flat=True)]
        total_vote_mean=sum(votes)/len(votes)
        vote_counts=[int(i) for i in Movie.objects.values_list('vote_count',flat=True)]
        vote_count_threshold=np.quantile(vote_counts,0.9)
        print(vote_count_threshold)
         """
        #TODO: Calculate this value evertime when a movie added to system or any vote given to movie
        total_vote_mean=3.120521702689949
        vote_count_threshold=15.0
        ###todo end

        #getting Qualified Movies
        qualified_movies=Movie.objects.filter(vote_count__gte=vote_count_threshold).values('id','vote_count','vote_average')
        for i in range(len(qualified_movies)):
            qualified_movies[i]['score']=(float(qualified_movies[i]['vote_count'])/(float(qualified_movies[i]['vote_count'])+vote_count_threshold)*float(qualified_movies[i]['vote_average']))+(vote_count_threshold/(vote_count_threshold+float(qualified_movies[i]['vote_count']))*total_vote_mean)
        qualified_movies=sorted(qualified_movies,key=lambda i:i['score'])[-10:]
        return Response({'timeline':'this week','movies':qualified_movies},status=status.HTTP_200_OK)

#PeopleDetails
class PersonDetailView(APIView):
    def get(self,request,pk):
        person=get_object_or_404(Person,id=pk)
        serializer=PersonSerializer(person)
        return Response(serializer.data,status=status.HTTP_200_OK)

#MovieSearch
from django.contrib.postgres.search import SearchQuery,SearchRank,SearchVector
from django.db import connection
class MovieSearch(APIView):
    def get(self,request):
        query=self.request.query_params.get("query")
        sv=SearchVector('title','credit__cast__character')
        sq=SearchQuery('Iron')
        cursor=connection.cursor()
        cursor.execute("select mm.id from movie_cast mc join movie_credit_cast mcc on (mcc.cast_id=mc.id) join movie_movie mm on (mm.id=mcc.credit_id) where mc.character like '%{0}%'".format(query))
        movies_list=[ids[0] for ids in cursor.fetchall()]
        cursor.execute("select mm.id from movie_crew mc join movie_credit_crew mcc on (mcc.crew_id=mc.id) join movie_movie mm on (mm.id=mcc.credit_id) where mc.name like '%{0}%' and mc.job='Director'".format(query))
        movies_list=movies_list+[ids[0] for ids in cursor.fetchall()]
        movies=Movie.objects.filter(id__in=movies_list).values('id','title','vote_average','vote_count').order_by('-popularity')
        return Response(movies,status=status.HTTP_200_OK)