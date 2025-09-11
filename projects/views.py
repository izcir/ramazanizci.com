from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related_projects = Project.objects.filter(is_active=True).exclude(slug=slug)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/detail.html', context)
