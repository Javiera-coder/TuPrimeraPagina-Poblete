from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def otra(request):
    return render(request, 'otra.html')
