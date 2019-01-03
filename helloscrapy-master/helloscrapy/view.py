# -*- coding: utf-8 -*-
from django.http import HttpResponse   #not MTV or MVC, data and view not indepedant
from django.shortcuts import render     # MTV  

def hello(request):
    return HttpResponse("Hello world ! ")       #not MTV or MVC, data and view not indepedant 

def newhello(request):
    context          = {}
    context['hello'] = 'Hello World!'       #context: dictory ,  key = hello = "{{ hello }}" in template , value = 'Hello World!'
    return render(request, 'hello.html', context)       # render use 'context(dictory)' as param

