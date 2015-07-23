from django.contrib import admin

# Register your models here.
from .models import Unit,Connection

admin.site.register(Unit)
admin.site.register(Connection)