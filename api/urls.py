from django.urls import path
from . import views

app_name='api'

urlpatterns=[
    path('movie/<int:pk>',views.MovieDetailView.as_view(),name='movie_detail'),
    path('movie/popular',views.PopularMovies.as_view(),name='popular_movie'),
    path('people/<int:pk>',views.PersonDetailView.as_view(),name='people_detail'),
    path('movie/search',views.MovieSearch.as_view(),name='movie_search'),
]