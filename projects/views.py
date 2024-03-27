from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import CreateProjectForm


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list_projects.html", context)


@login_required
def show_project(request, id):
    show_project = Project.objects.get(id=id)
    context = {"project": show_project}
    return render(request, "projects/show_project.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            projects = form.save(False)
            projects.owner = request.user
            projects.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
    context = {"form": form}
    return render(request, "projects/create_project.html", context)
