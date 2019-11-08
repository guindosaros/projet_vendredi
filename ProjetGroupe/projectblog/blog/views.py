from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def category(request):
    return render(request, 'pages/category.html')

def regulare(request):
    return render(request, 'pages/regulare.html')

def single(request):
    return render(request, 'pages/single.html')

