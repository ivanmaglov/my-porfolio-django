from django.shortcuts import render,get_object_or_404
from .models import Projects
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
# Create your views here.
def allprojects(request):
    projects_list = Projects.objects.all().order_by('-pub_date')[:40]
    paginator = Paginator(projects_list, 3)  # Show 3 projects per page
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    return render(request, 'allprojects.html', {'projects': projects})

def home(request):
    projects=Projects.objects.all().order_by('-pub_date')[:3]
    return render(request, 'homepage.html', {'projects': projects })

def detail(request,projects_id):
    projects=get_object_or_404(Projects, pk=projects_id)
    return render(request, 'detail.html', {'projects': projects})