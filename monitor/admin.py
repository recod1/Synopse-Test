from django.contrib import admin
from .models import Mikrot, GlobalGroup, Group
# Register your models here.

admin.site.register(GlobalGroup)
admin.site.register(Group)
admin.site.register(Mikrot)