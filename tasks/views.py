from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            category = form.save()
            category.assignee = request.user
            category.save()
            return redirect("list_projects")
    else:
        form = TaskForm
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    show_my_tasks = Task.objects.filter(assignee=request.user)
    context = {"my_tasks": show_my_tasks}
    return render(request, "tasks/show_my_tasks.html", context)
