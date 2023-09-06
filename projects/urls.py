from django.urls import path
from projects.views import show_projects_list

urlpatterns = [path("", show_projects_list, name="list_projects/")]
