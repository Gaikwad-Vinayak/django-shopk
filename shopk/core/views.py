from django.shortcuts import render
from .forms import regi
# Create your views here.
def indext(request):
    return render(request,'core/index.html')

def collection(request):
    return render(request,'core/collection.html')

def shoes(request):
    return render(request,'core/shoes.html')


def contact(request):
    return render(request,'core/contact.html')


def recing(request):
    return render(request,'core/racing_boots.html')


def register(request):
    form=regi()    
    return render(request,'core/register.html',{'form':form})