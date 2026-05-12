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


def project_detail_en(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related_projects = Project.objects.filter(is_active=True).exclude(slug=slug)[:3]

    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/detail_en.html', context)


def project_list(request):
    """Tüm aktif projeleri listele"""
    projects = Project.objects.filter(is_active=True).order_by('order', '-created_at')
    context = {
        'projects': projects,
    }
    return render(request, 'projects/list.html', context)


def project_list_en(request):
    """List all active projects (EN)"""
    projects = Project.objects.filter(is_active=True).order_by('order', '-created_at')
    context = {
        'projects': projects,
    }
    return render(request, 'projects/list_en.html', context)
