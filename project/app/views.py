from django.shortcuts import render
from .forms import Userform, AddPost
from django.http import HttpResponse
from .models import Person, Posts



def posts(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        is_published = request.POST.get('is_published')
        url = request.POST.get('url')
        one = Posts.objects.create(title=title, text=text, is_published=is_published, url=url)
        post = Posts.objects.all()
        return render(request, post.html, context={'posts': post})
    else:
        form = AddPost
        return render(request, 'post.html', context={'form':form})



def data(request):
    tom = Person.objects.get_or_create(name='Tom', age=14, date='2015-02-03', agree=False)

    try:
        mike = Person.objects.get(name='Mike')
        mike.delete()
    except:
        mike = Person(name='Mike', age=25, date='2015-02-03 10:33', agree=True)
        mike.save()
    data = Person.objects.filter(age__gt=20)
    return render(request, 'data.html', context={'data': data})

def index(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            return HttpResponse(f' {name} поздравляю с регистрацией!')
        else:
            return HttpResponse('Данные не валидны')
    else:
        form = Userform()
        return render(request, 'index.html', context={'form': form})


def log(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            return HttpResponse(f' Поздравляю с успешным входом!!!')
        else:
            return HttpResponse('Данные не валидны')
    else:
        form = Userform()
        return render(request, 'log.html', context={'form': form})