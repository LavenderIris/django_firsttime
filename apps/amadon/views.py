from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):

    return render(request,'amadon/index.html')

def buy(request):
    

    if request.method == 'POST':
        myrequest =  request.POST
        print "myrequest", myrequest
        print 'product', myrequest['quantity'][0]
        request.session['quantity']=myrequest['quantity'][0]
        if (myrequest['product_id'][0] == '1'):
            request.session['price']=19.99
        elif (myrequest['product_id'][0] == '2'):
            request.session['price']=29.99
        elif (myrequest['product_id'][0] == '3'):
            request.session['price']=4.99
        elif (myrequest['product_id'][0] == '4'):
            request.session['price']=49.99
        request.session['total']= request.session['price'] *  int(request.session['quantity'])
        print ('session', request.session['price'])
        print ('session', request.session['quantity'])
        if 'count' not in request.session:
            request.session['count'] = int(request.session['quantity'])
        else :
            request.session['count'] += int(request.session['quantity'])
        if 'total_so_far' not in request.session:
            request.session['total_so_far'] = request.session['total'] 
        else: 
            request.session['total_so_far'] += request.session['total'] 
    return redirect('/amadon/checkout')

def reset(request):

    if request.method=='GET':       
        request.session.clear()
    return redirect('/amadon')

def checkout(request):
    return render(request,'amadon/result.html')
