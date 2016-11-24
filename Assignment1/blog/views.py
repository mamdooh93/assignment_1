from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import example1
from django.http import JsonResponse


def show_example1(request):
    return render(request, "example1.html", {"d": example1})


def get_example1(request):

    from django.http import JsonResponse
     #   return HttpResponse(example1)
      #  return HttpResponse( json.dumps( data ) )
    example1= {'Django':'Django is a Python based full stack web development framework means it is used to develop full fledged websites in Python. it encourages rapid development and advocates pragmatic and clean code.','Python':'Python is a general purpose programming language created in the late 1980s, and named after Monty Python, thats used by thousands of people to do things from testing microchips at Intel to powering Instagram, to building video games with the PyGame library',
           'Java':'Java is a programming language that developers use to create applications on your computer. Chances are youve downloaded a program that required the Java runtime, and so you probably have it installed it on your system. Java also has a web plug-in that allows you to run these apps in your browser','C++':'Most packaged software is still written in C++. That means games, office applications, graphics and video editors, and operating systems. In fact, if you think of the software you use every day that isnt online, chances are it is written in C++ (or C or objective-C). Its not written in Java, Python, Ruby, Perl, etc.'
           ,'C#':'Firstly it is important to note that C# is just one of several languages that can be used with the Microsoft .NET Framework. Many of the advantages and features of C# are actually tied very closely to .NET, and hence are also applicable to languages like Visual Basic .NET and Visual C++ .NET'}
    return JsonResponse(example1, status=201)