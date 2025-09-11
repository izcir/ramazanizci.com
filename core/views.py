from django.shortcuts import render
from projects.models import Project
from skills.models import Skill

def home(request):
    projects = Project.objects.filter(is_active=True)
    skills = Skill.objects.filter(is_active=True)
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'core/home.html', context)
