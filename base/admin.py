from django.contrib import admin
from base.models import Person
from base.models import Client
from base.models import Venue
from base.models import Events
from base.models import Employees
from base.models import Post
from base.models import Type_of_diagnoses
from base.models import Visits

# Register your models here.

admin.site.register(Person)
admin.site.register(Client)
admin.site.register(Venue)
admin.site.register(Events)
admin.site.register(Employees)
admin.site.register(Post)
admin.site.register(Type_of_diagnoses)
admin.site.register(Visits)