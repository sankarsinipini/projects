from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello Django")
    return render(request, 'pages/index.html')

def about(request):
    name="Jhon"
    students = {
        1 : {"name": "Jhon", "cgpa": 9.3},
        2 : {"name": "Sara", "cgpa": 9.5},
        3 : {"name": "Sam", "cgpa": 8.2}
    }
    context = {
        "myname": name,
        "num": 21,
        "drinks": ['tea', 'coffee', 'fruit juice', 'cold coffee'],
        "students": students
    }
    return render(request, 'pages/about.html', context)
