from multiprocessing import context
from django.shortcuts import render
from .models import Project
# Create your views here.

def getProjects(request):
    projects = Project.objects.all
    context = {
        'products': projects
    }
    return render(request, 'portfolio/index.html',context)
