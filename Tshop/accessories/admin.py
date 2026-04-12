from django.contrib import admin
from .models import Accessory, AccessoryCategory

# Register your models here.
admin.site.register(Accessory)
admin.site.register(AccessoryCategory)