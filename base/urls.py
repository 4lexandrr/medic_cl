from argparse import Namespace
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),


    path('user_profile/<str:pk>/', views.UserProfile, name='user-profile'),
    path('update_profile/<str:pk>/', views.update_profile, name='update-profile'),

    path('doctors/', views.doctors_list, name='doctor-list'),
    path('doctors/<str:id>/', views.reception, name='datetime'),
    path('doctors/<str:id>/available_time', views.available_time, name='available-time'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('events/', views.all_events, name='list-events'),
    path('add_events/', views.add_events, name='add-events'),
    path('update_events/<event_id>', views.update_events, name='update-events'),
    path('delete_events/<event_id>', views.delete_events, name='delete-events'),

    path('venue/', views.all_venue, name='all-venue'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),

    path('products/', views.cart, name='products'),
    path('add_test/', views.add_test, name='add-test'),
    path('update_test/<test_id>', views.update_test, name='update-test'),
    path('delete_test/<test_id>', views.delete_test, name='delete-test'),
    path('check_out', views.order, name='check-out'),
]