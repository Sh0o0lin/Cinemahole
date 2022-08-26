from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Movies/',include('movie.urls',namespace='movie')),
    path('api/',include('api.urls',namespace='api')),
    path('',include('atani.urls',namespace='atani')),
]
