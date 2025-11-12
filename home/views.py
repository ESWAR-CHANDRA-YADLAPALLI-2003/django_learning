from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h2>Welcome to Django Learning</h2>")
    return render(request, 'index.html')
def about(request):
    return HttpResponse("<h2>About Page</h2><p>This is my first Django project.</p>")
def contact(request):
    return render(request, 'contact.html')

