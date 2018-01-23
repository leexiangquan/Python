from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
	return HttpResponse("Hello world! I am coming soon. This is the first Djaongo test by Quan X.L")

