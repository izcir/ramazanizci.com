from django.db import models

class Skill(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Başlangıç'),
        ('intermediate', 'Orta'),
        ('advanced', 'İleri'),
        ('expert', 'Uzman'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Yetenek Adı")
    description = models.TextField(verbose_name="Açıklama")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Seviye")
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class", verbose_name="İkon")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Yetenek"
        verbose_name_plural = "Yetenekler"

    def __str__(self):
        return self.name
