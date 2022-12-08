from csv import Dialect
from pydoc import Doc
from telnetlib import DO
from django.contrib import admin
from base.models import User
from base.models import Venue
from base.models import Events
from base.models import Post
from base.models import Tests, UserItem
from base.models import Type_of_diagnoses
from base.models import Visits
from base.models import Doctor
from base.models import Reception
from base.models import AvailableTime
from base.models import Order




# Register your models here.

admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Events)
admin.site.register(Post)
admin.site.register(Tests)
admin.site.register(UserItem)
admin.site.register(Type_of_diagnoses)
admin.site.register(Visits)
admin.site.register(Doctor)
admin.site.register(Reception)
admin.site.register(AvailableTime)
admin.site.register(Order)

