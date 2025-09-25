from django.contrib import admin
from .models import Contact, CustomUser
# Register your models here.

admin.site.register(Contact)
admin.site.register(CustomUser)