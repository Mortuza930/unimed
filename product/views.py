from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'product/home.html')

def tablet(request):
    return render(request, 'product/tablet.html')

def capsule(request):
    return render(request, 'product/capsule.html')

def pfs(request):
    return render(request, 'product/pfs.html')

def syrup(request):
    return render(request, 'product/syrup.html')





