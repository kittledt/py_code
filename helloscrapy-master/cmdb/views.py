from django.shortcuts import render # MTV 
#from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hello index ! ")
    
    #context          = {}
    #context['hello'] = 'Hello World!'       #context: dictory ,  key = hello = "{{ hello }}" in template , value = 'Hello World!'
    return render(request, 'index.html')       # render use 'context(dictory)' as param