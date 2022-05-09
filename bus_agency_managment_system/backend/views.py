from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'backend/login.html')

def dashboard(request):
    return render(request, 'backend/index.html')