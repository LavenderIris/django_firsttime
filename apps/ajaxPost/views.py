from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
import random
from .models import Note

def index(request):
    return render(request,'index.html')

def create(request):
    Note.objects.create(content=request.POST['note'])
    notes = Note.objects.all()
    print('in create')
    return render(request, 'all.html', {'notes':notes})

