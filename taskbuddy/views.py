from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProjectForm

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'pages/dashboard/projects.html', {'projects': projects})

def colleagues(request):
    return render(request, 'pages/dashboard/colleagues.html')

def tasks(request):
    return render(request, 'pages/dashboard/tasks.html')

def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'pages/dashboard/new-project.html', {'form': form})

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('edit_project', project_id=project_id)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'pages/dashboard/edit_project.html', {'form': form, 'project': project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect('projects')