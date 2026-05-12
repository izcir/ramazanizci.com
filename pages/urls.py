from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('en/contact/', views.contact_en, name='contact_en'),
]
