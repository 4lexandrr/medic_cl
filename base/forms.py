from dataclasses import field
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Events, Tests, Venue, User, Reception


class ReceptionForm(ModelForm):
    class Meta:
        model = Reception
        time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        fields = ('user', 'doctor', 'date', 'time')  # Либо в () вводим нужные нам поля из модели

        labels = {
            'user': 'Клиент: ',
            'doctor': 'Доктор: ',
            'date': 'Дата: ',
            'time': 'Время: '
        }

        


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'years', 'email', 'polis', 'mobile_phone', 'registration_address']

        labels = {
            'first_name': 'Имя',
            'middle_name': 'Отчество',
            'last_name': 'Фамилию',
            'years': 'Год рождения',
            'email': 'Электронная почта',
            'polis': 'Медицинский полис',
            'mobile_phone': 'Контактный номер',
            'registration_address': 'Адрес регистрации',
        }



class VenueForm(ModelForm):
    ''' Создаём класс VenueForm для отображения формы на сайте '''
    class Meta:
        model = Venue
        fields = '__all__'  # Либо в () вводим нужные нам поля из модели

        labels = {
            'name': 'Введите название собития',
            'address': 'Введите адрес',
            'zip_code': 'Введите индекс',
            'phone': 'Введите контактный номер',
        }


class EventForm(ModelForm):
    ''' Создаём класс VenueForm для отображения формы на сайте '''
    class Meta:
        model = Events
        fields = '__all__'  # Либо в () вводим нужные нам поля из модели

        labels = {
            'name': 'Введите название собития',
            'event_date': 'Выберите дату',
            'venue': 'Выберите место проведения',
            'docror': 'Выберите врача',
            'description': 'Напишите пожелания или жалобы',
            'attendes': 'Выберите клиента ' 
        }

        

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название собития'}), 
        #     'event_date': forms.TextInput(attrs={'class': 'form-control'}), 
        #     'venue': forms.TextInput(attrs={'class': 'form-control'}), 
        #     'doctor': forms.TextInput(attrs={'class': 'form-control'}), 
        #     'description': forms.TextInput(attrs={'class': 'form-control'}), 
        #     'attends': forms.TextInput(attrs={'class': 'form-control'}), 
        # }

class TestForm(ModelForm):
    ''' Создаём класс VenueForm для отображения формы на сайте '''
    class Meta:
        model = Tests
        fields = '__all__'  # Либо в () вводим нужные нам поля из модели

        labels = {
            'name': 'Введите название собития',
            'description': 'Напишите пожелания или жалобы',
            'cost': ' Стоимость ' 
        }
