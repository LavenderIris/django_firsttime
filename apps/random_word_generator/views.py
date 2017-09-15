from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



def index(request):
    
    print "got to index"
   
    request.session['word'] = get_random_string(length=14)
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    print "request", request.session['word']
    return render(request,'random_word_generator/index.html')


def reset(request):
    request.session['count']=0
    return redirect('/random_word')

def generate(request):
    return redirect('/random_word')