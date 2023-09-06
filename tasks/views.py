from django.shortcuts import render, redirect
from tasks.forms import CreateTaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            category = form.save()
            category.owner = request.user
            category.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/detail.html", context)
