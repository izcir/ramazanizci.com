from django.shortcuts import render
from projects.models import Project
from skills.models import Skill

def home(request):
    projects = Project.objects.filter(is_active=True).order_by('order', '-created_at')[:6]
    skills = Skill.objects.filter(is_active=True)
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'core/home.html', context)
