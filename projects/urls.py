from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('tum-projeler/', views.project_list, name='list'),
    path('proje/<slug:slug>/', views.project_detail, name='detail'),
]
