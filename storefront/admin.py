from django.contrib import admin

from .models import Books
from .models import Languages,Genres

admin.site.register(Books)
admin.site.register(Languages)
admin.site.register(Genres)
