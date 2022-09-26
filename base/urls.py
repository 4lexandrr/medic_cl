from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('page/<str:pk>/', views.room)
]