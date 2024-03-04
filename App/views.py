from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
 

def index(request):
    #return HttpResponse("<h1>hey there you are connect @@@<h1>")
    return render(request,'index.html',)
def index1(request):
    return render(request,'404.html',)
def index2(request):
    return render(request,'cart.html',)
def index5(request):
    return render(request, 'shop-detail.html',)
def index6(request):
    return render(request, 'shop.html',)
def index7(request):
    return render(request, 'testimonial.html',)
def index4(request):
    if request.method == 'POST':
        form = ContactDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added successfully')
        else:
            return HttpResponse(form.errors)
    else:
        form = ContactDetailForm()
    return render(request, 'contact.html', {'form': form})
def index3(request):
    if request.method == 'POST':
        form = CustomerDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added successfully')
        else:
            return HttpResponse(form.errors)
    else:
        form = CustomerDetailForm()
    return render(request, 'checkout.html', {'form': form})