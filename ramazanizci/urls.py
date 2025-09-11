"""
URL configuration for ramazanizci project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

admin_url = os.environ.get('ADMIN_URL', 'admin/')

urlpatterns = [
    path(admin_url, admin.site.urls),
    path('', include('core.urls')),
    path('', include('pages.urls')),
    path('', include('projects.urls')),
    path('robots.txt', serve, {'path': 'robots.txt', 'document_root': settings.STATIC_ROOT}),
    path('sitemap.xml', serve, {'path': 'sitemap.xml', 'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
