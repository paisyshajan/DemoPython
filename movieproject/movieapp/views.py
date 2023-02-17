from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={'movie_list':movie}
    return render(request,'index.html',context)
def details(request,movie_id):
    # return HttpResponse('this is movie no %s' % movie_id)

      movie=Movie.objects.get(id=movie_id)
      return render(request,'details.html',{'movy':movie})

def add_movie(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Description = request.POST.get('desc',)
        Year = request.POST.get('year',)
        Image = request.FILES['img']
        movie=Movie(name=Name,desc=Description,year=Year,img=Image)
        movie.save()
    return render(request,'add.html')


def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None , request.FILES, instance=movie)
    if form . is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'frm':form,'movy':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
