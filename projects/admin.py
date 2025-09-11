from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'technologies', 'order', 'created_at', 'readme_url']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'technologies', 'technical_details']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'slug', 'description', 'technologies', 'about_html')
        }),
        ('Struktürel Bilgiler', {
            'fields': ('project_info', 'features', 'technical_details')
        }),
        ('Linkler', {
            'fields': ('github_link', 'demo_link', 'readme_url')
        }),
        ('Görsel ve Ayarlar', {
            'fields': ('image', 'order')
        }),
    )
