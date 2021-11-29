from django.shortcuts import render
from django.views.generic import View

from .models import GlobalGroup
from .visit_info import change_info


class GlobalGroupList(View):

	def get(self, request):
		
		group_global = GlobalGroup.objects.all()
		change_info(request)
		return render(request, "monitor/index.html", {'group_global':group_global})

