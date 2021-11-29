from django.contrib import admin
from .models import Mikrot, GlobalGroup, Group, Userip, VisitNumber, DayNumber
# Register your models here.


admin.site.register(Userip)
admin.site.register(VisitNumber)
admin.site.register(DayNumber)
admin.site.register(GlobalGroup)
admin.site.register(Group)
admin.site.register(Mikrot)
