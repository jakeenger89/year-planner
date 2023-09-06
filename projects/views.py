from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import CreateProjectForm

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


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()

    context = {
        "form": form,
    }

    return render(request, "create.html", context)
