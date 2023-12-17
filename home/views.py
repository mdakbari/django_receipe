from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    pe = [
        {'name': 'akbari', 'age':'21'},
        {'name': 'manthan', 'age':'21'}
    ]
    for p in pe:
        print(p)
    return render(request, "index.html", context={'pe' : pe})


def new(request):
    return render(request, "home.html")
