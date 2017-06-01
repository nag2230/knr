from django.shortcuts import render
from django.http import HttpResponse
'''def index(request):
    return HttpResponse("HELLO<br><a href='/rango/about/')>About</a>")'''
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    return HttpResponse("rango says This is about page&nbsp: <a href='/rango/'>Back</a>")
