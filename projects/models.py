from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Proje Başlığı (EN)")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL Slug")
    description = models.TextField(verbose_name="Açıklama")
    description_en = models.TextField(blank=True, verbose_name="Açıklama (EN)")
    technologies = models.CharField(max_length=300, verbose_name="Kullanılan Teknolojiler")
    technologies_en = models.CharField(max_length=300, blank=True, verbose_name="Kullanılan Teknolojiler (EN)")
    about_html = models.TextField(blank=True, verbose_name="Proje Hakkında (HTML)")
    about_html_en = models.TextField(blank=True, verbose_name="Proje Hakkında (HTML) (EN)")
    project_info = models.JSONField(blank=True, null=True, default=dict, verbose_name="Proje Bilgileri")
    project_info_en = models.JSONField(blank=True, null=True, default=dict, verbose_name="Proje Bilgileri (EN)")
    features = models.JSONField(blank=True, null=True, default=list, verbose_name="Öne Çıkan Özellikler")
    features_en = models.JSONField(blank=True, null=True, default=list, verbose_name="Öne Çıkan Özellikler (EN)")
    technical_details = models.TextField(blank=True, verbose_name="Teknik Detaylar")
    technical_details_en = models.TextField(blank=True, verbose_name="Teknik Detaylar (EN)")
    readme_url = models.URLField(blank=True, null=True, verbose_name="README Linki")

    github_link = models.URLField(blank=True, null=True, verbose_name="GitHub Linki")
    demo_link = models.URLField(blank=True, null=True, verbose_name="Demo Linki")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Proje Görseli")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})
