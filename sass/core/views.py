from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwrd_args):
    return render(request, 'home.html')