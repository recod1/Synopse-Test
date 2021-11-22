from django.shortcuts import render
from django.views.generic import View

from .models import GlobalGroup


class GlobalGroupList(View):

	def get(self, request):
		group_global = GlobalGroup.objects.all()
		return render(request, "monitor/index.html", {'group_global':group_global})