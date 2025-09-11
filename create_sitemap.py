import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ramazanizci.settings')
django.setup()

from projects.models import Project
from django.conf import settings
from django.urls import reverse

BASE_URL = os.environ.get('SITE_URL', 'https://ramazanizci.com')

sitemap_path = os.path.join(settings.BASE_DIR, 'static', 'sitemap.xml')

urls = [
    f"{BASE_URL}/",
]

for project in Project.objects.filter(is_active=True):
    urls.append(f"{BASE_URL}/proje/{project.slug}/")

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in urls:
        f.write('  <url>\n')
        f.write(f'    <loc>{url}</loc>\n')
        f.write('  </url>\n')
    f.write('</urlset>\n')
print(f"Sitemap generated at {sitemap_path}")
