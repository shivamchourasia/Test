from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse("Hello World!, Starting new project")
    #return render(request, "sample.html")
