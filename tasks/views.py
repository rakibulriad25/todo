import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from urllib3 import HTTPResponse
from tasks.models import Create
from django.urls import reverse
# Create your views here.

def home(request):
    titles = Create.objects.all().values()
    desc = request.GET.get('desc')

    return render(request, 'home.html', {'titles': titles, 'desc': desc})

def create(request):
    return render(request, 'create.html')

def createrecord(request):
    title = request.POST['title']
    desc = request.POST['desc']

    task = Create(title=title, desc=desc)
    task.save()

    return HttpResponseRedirect(reverse('home'))

def delete(request, id):
    task = Create.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('home'))

def edit(request, id):
    x = Create.objects.get(id=id)
    return render(request, 'edit.html', {'x': x})
def editrecord(request, id):
    title = request.POST['title']
    desc = request.POST['desc']

    x = Create.objects.get(id=id)
    x.title = title
    x.desc = desc
    x.save()

    return HttpResponseRedirect(reverse('home'))