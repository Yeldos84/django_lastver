from django.contrib import admin
from .models import Parent, Child, Icecream, HumanInfo, Kiosk
# Register your models here.
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Icecream)
admin.site.register(Kiosk)
