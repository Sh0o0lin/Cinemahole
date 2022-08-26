from django.shortcuts import render,get_object_or_404
from .models import Movie
from .forms import ModelForm, MovieForm
from django.forms.models import model_to_dict

def error_404(request,exception):
        data = {}
        return render(request,'Movie/ErrorPage/404.html', data)

def error_500(request):
        data = {}
        return render(request,'Movie/ErrorPage/500.html', data)

def home(request):
    popular_movies=[355602,26669,355593,11210,35944,355592,30390,355584,119082,342400]
    movies=Movie.objects.filter(id__in=popular_movies)
    return render(request,'movie/home.html',{'movies':movies})

def details(request,pk):
        movie=get_object_or_404(Movie,id=pk)
        return render(request,'movie/details.html',{'movie':movie})

def edit(request,pk):
        movie=get_object_or_404(Movie,id=pk)
        if request.method=='POST':
                form=MovieForm(request.POST,request.FILES)
                if form.is_valid():
                        print("lol")
        else:
                
                form=MovieForm(initial=model_to_dict(movie))
        context={'form':form,'movie':movie}
        return render(request,'movie/edit.html',context)