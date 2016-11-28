from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Ohai, this is polls index")

# Create your views here.
