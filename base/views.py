from pydoc import Doc, doc
from urllib.request import Request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import RedirectView
from .models import Venue, Events, User, Tests, Doctor, Reception, AvailableTime
from .forms import EventForm, VenueForm, MyUserCreationForm, ProfileForm, TestForm, ReceptionForm
# Create your views here.


@login_required(login_url='login')
def available_time(request, id):
    date = request.POST['date']
    times = AvailableTime.objects.filter(doctor__id=id, date=date, is_active=True)
    context = {'times': times}
    return render(request, 'base/available_time.html', context)


@login_required(login_url='login')
def reception(request, id):
    form = ReceptionForm(request.POST)
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':

        if form.is_valid():
            save = form.save(commit=False)
            save.user = request.user
            if Reception.objects.filter(time=save.time, date=save.date, doctor=save.doctor, user=save.user):
                messages.error(request, 'Запись уже есть')
                return redirect('doctor-list')
            else:

                save.save()
                doctor = Doctor.objects.get(user=save.doctor.user)
                doctor.receptions.add(save)
                messages.success(request, 'Запись успешно добавлена!')
                return redirect('doctor-list')
        else:
            messages.info(request, 'Ошибка формы')
    
    context = {'form': form, 'doctor': doctor, 'id': id}
    return render(request, 'base/datetimepicker.html', context)


def home(request):
    return render(request, 'base/home.html')


@login_required(login_url='login')
def doctors_list(request):
    doctor_list = Doctor.objects.all()
    context = {'doctor_list': doctor_list}
    return render(request, 'base/doctors_list.html', context)


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
def all_events(request):
    event_list = Events.objects.all()
    context = {'event_list': event_list}
    return render(request, 'base/events_list.html', context)


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


@login_required
def cart(request):
    products = Tests.objects.all()
    context = {'products': products}
    return render(request, 'base/cart.html', context)


@login_required(login_url='login')
def add_test(request):
    submitted = False
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_test?submitted=True')

    else:
        form = TestForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base/add_test.html', {'form': form, 'submitted': submitted})


@login_required(login_url='login')
def update_test(request, test_id):
    test = Tests.objects.get(pk=test_id)
    form = TestForm(request.POST or None, instance=test)
    context = {'event': test, 'form': form}

    if form.is_valid():
        form.save()
        return redirect('all-tests')

    return render(request, 'base/update_test.html', context)


@login_required(login_url='login')
def delete_test(request, test_id):
    test = Events.objects.get(pk=test_id)
    context = {'obj': test}
    if request.method == 'POST':
        test.delete()
        return redirect('all-tests')

    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def UserProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'base/user_profile.html', context)


@login_required(login_url='login')
def update_profile(request, pk):
    user = User.objects.get(id=pk)
    form = ProfileForm(request.POST or None, instance=user)
    context = {'user': user, 'form': form}

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'base/update_profile.html', context)


def user_login(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')


    return render(request, 'base/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Недопустимый логин и/или пароль')

    return render(request, 'base/login_register.html', {'form': form}) 


    




