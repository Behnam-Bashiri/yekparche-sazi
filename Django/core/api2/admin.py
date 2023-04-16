from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Base_device)
admin.site.register(Phone)
admin.site.register(Laptop)
admin.site.register(Tablet)
admin.site.register(Cpu)