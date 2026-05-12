from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('tum-projeler/', views.project_list, name='list'),
    path('proje/<slug:slug>/', views.project_detail, name='detail'),
    path('en/projects/', views.project_list_en, name='list_en'),
    path('en/project/<slug:slug>/', views.project_detail_en, name='detail_en'),
]
