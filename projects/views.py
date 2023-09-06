from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {"list_projects": list_projects}
    return render(request, "list.html", context)


@login_required
def show_project(request, id):
    show_project = Project.objects.get(id=id)
    context = {
        "show_project": show_project,
    }
    return render(request, "detail.html", context)
