from django.contrib import admin
from movieratings.models import Rater, Item, Data

admin.site.register([Rater, Item, Data])
# Register your models here.
