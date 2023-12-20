from projects.models import Project

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list_projects(request):
    list_of_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_of_projects": list_of_projects,
    }
    return render(request, "projects/list_projects.html", context)


@login_required
def show_project(request, id):
    project_details = Project.objects.get(id=id)
    context = {"project_details": project_details}
    return render(request, "projects/project_details.html", context)
