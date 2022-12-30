from django.shortcuts import render
from django.http import HttpResponse
from django import template

# Create your views here.
def home(request):
    '''
    Without response type returning just 'Hello wrold' (540b)
    Wit response type "text/plain" returning 'Hello world' with <pre> around(540b)
    '''
    # return HttpResponse('Hello, world!\n')
    return HttpResponse('Hello, world!\n', content_type="text/plain")


def home_index(request):
    return render(request, 'templates/static_handler.html')
