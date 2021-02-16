from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("This is my Homepage (/)")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Thiss is my Homepage (/)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is mssy Homepage (/)")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("This is my Homepage (/)")
    return render(request, 'contact.html')