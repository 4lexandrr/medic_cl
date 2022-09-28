import imp
from unicodedata import name
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm
from .models import Client, Venue
from .models import Events
from .forms import EventForm
from .forms import VenueForm
# Create your views here.

from django.http import HttpResponse


def all_venue(request):
    venue_list = Venue.objects.all()
    context = {'venue_list': venue_list}
    return render(request, 'base/organization.html', context)

@login_required(login_url='login')
def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base/add_organization.html', {'form': form, 'submitted': submitted})


@login_required(login_url='login')
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    context = {'venue': venue, 'form': form}

    if form.is_valid():
        form.save()
        return redirect('all-venue')

    return render(request, 'base/update_organization.html', context)


@login_required(login_url='login')
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    context = {'obj': venue}
    if request.method == 'POST':
        venue.delete()
        return redirect('all-venue')

    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def add_events(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_events?submitted=True')

    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base/add_events.html', {'form': form, 'submitted': submitted})


@login_required(login_url='login')
def update_events(request, event_id):
    event = Events.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    context = {'event': event, 'form': form}

    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'base/update_events.html', context)


@login_required(login_url='login')
def delete_events(request, event_id):
    event = Events.objects.get(pk=event_id)
    context = {'obj': event}
    if request.method == 'POST':
        event.delete()
        return redirect('list-events')

    return render(request, 'base/delete.html', context)

    
def personal(request):
    profile = Client.objects.all()
    context = {'profile': profile}
    return render(request, 'base/personal_cab.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Неверный логин и/или пароль')
            else:
                messages.error(request, 'Неверный логин и/или пароль')
    else:
        form = LoginForm()
        
    return render(request, 'base/login_register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'base/home.html')


def all_events(request):
    event_list = Events.objects.all()
    context = {'event_list': event_list}
    return render(request, 'base/events_list.html', context)



