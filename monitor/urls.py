from django.urls import path

from . import views


urlpatterns = [
	path("", views.GlobalGroupList.as_view())
]