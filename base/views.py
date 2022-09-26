from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

pages = [
    {'id': 1, 'name': 'Личный кабинет'},
    {'id': 2, 'name': 'Запись к врачу'},
]


def home(request):
    context = {'pages': pages}
    return render(request, 'base/home.html', context)

def room(request, pk):
    page = None
    for i in pages:
        if i['id'] == int(pk):
            page = i
    context = {'page': page}
    return render(request, 'base/room.html', context)