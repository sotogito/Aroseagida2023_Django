from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def aroseagida(request):
    return render(request, 'pages/aroseagida.html')

def adventure(request):
    return render(request, 'pages/adventure.html')