from django.urls import path
from . import views

app_name='movie'

urlpatterns=[
    path('',views.home,name='CinemaHole'),
    path('<int:pk>',views.details,name='details'),
    path('edit/<int:pk>',views.edit,name='edit')
]