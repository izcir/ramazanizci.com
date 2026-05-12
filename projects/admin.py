from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'technologies', 'order', 'created_at', 'readme_url']
    list_filter = ['created_at']
    search_fields = ['title', 'title_en', 'description', 'description_en', 'technologies', 'technologies_en', 'technical_details', 'technical_details_en']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'slug', 'description', 'technologies', 'about_html')
        }),
        ('English İçerik', {
            'fields': ('title_en', 'description_en', 'technologies_en', 'about_html_en')
        }),
        ('Struktürel Bilgiler', {
            'fields': ('project_info', 'features', 'technical_details')
        }),
        ('Struktürel Bilgiler (EN)', {
            'fields': ('project_info_en', 'features_en', 'technical_details_en')
        }),
        ('Linkler', {
            'fields': ('github_link', 'demo_link', 'readme_url')
        }),
        ('Görsel ve Ayarlar', {
            'fields': ('image', 'order')
        }),
    )
