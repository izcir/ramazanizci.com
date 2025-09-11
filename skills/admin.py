from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'order', 'is_active']
    list_filter = ['level', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'description', 'level')
        }),
        ('Görünüm', {
            'fields': ('icon', 'order', 'is_active')
        }),
    )
