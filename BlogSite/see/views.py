from django.http import Http404,HttpResponse
from django.template import Template,Context
from django.shortcuts import render,render_to_response

# Create your views here.

def home(request):
    return render_to_response(r'home\home.html')

def blog(request):
    return render_to_response(r'blog\blog.html')

def contact(request):
    return render_to_response(r'contact\contact.html')

def about(request):
    return render_to_response(r'about\about.html')

def more(request):
    return render_to_response(r'more\more.html') 