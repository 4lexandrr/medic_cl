from django.contrib import admin
from base.models import Venue
from base.models import Events
from base.models import Post
from base.models import Type_of_diagnoses
from base.models import Visits
from base.models import User
from base.models import Tests


# Register your models here.

admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Events)
admin.site.register(Post)
admin.site.register(Tests)
admin.site.register(Type_of_diagnoses)
admin.site.register(Visits)
