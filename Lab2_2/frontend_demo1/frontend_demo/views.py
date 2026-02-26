from django.shortcuts import render

def index(request):
    return render(request, 'frontend_demo1/index.html')

# Create your views here.
