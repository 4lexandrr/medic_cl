from xml.etree.ElementInclude import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('personal_cab/', views.personal, name='personal'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('events/', views.all_events, name='list-events'),
    path('add_events/', views.add_events, name='add-events'),
    path('update_events/<event_id>', views.update_events, name='update-events'),
    path('delete_events/<event_id>', views.delete_events, name='delete-events'),
    path('venue/', views.all_venue, name='all-venue'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
]