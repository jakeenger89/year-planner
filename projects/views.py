from django.shortcuts import render
from projects.models import Project

# Create your views here.


def show_projects_list(request):
    project_list = Project.objects.all()
    context = {"project_list": project_list}
    return render(request, "list.html", context)
