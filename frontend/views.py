from django.shortcuts import render

def list(request):
    return render(request, 'frontend/index.html')

# Create your views here.
