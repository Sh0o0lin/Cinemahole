from django.urls import path
from . import views

app_name='atani'

urlpatterns = [
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
]