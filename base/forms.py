
from django import forms
from django.forms import ModelForm
from .models import Events
from .models import Venue


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


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

