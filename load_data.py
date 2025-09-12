#!/usr/bin/env python
"""
Örnek proje ve yetenek verilerini veritabanına ekleyen script
"""
import os
import sys
import django
from pathlib import Path

# Django'yu yapılandır
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ramazanizci.settings')
django.setup()

from projects.models import Project
from skills.models import Skill

# Content files base path
CONTENT_PATH = Path(__file__).parent / 'templates' / 'projects' / 'content'

def load_content_file(filename):
    """Content dosyasını yükle"""
    try:
        file_path = CONTENT_PATH / filename
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: {filename} dosyası bulunamadı!")
        return ""

def clear_data():
    """Mevcut verileri temizle"""
    print("Mevcut veriler temizleniyor...")
    Project.objects.all().delete()
    Skill.objects.all().delete()
    print("Veriler temizlendi.")

def create_projects():
    """Örnek projeler oluştur"""
    print("Projeler oluşturuluyor...")
    
    projects_data = [
        {
            'title': 'Sınavİzcisi',
            'slug': 'sinavizcisi-com',
            'description': 'YKS verilerini analiz eden ve yapay zekâ destekli tercih tahmini yapan web platformu. Django + PostgreSQL + Transformers kullanıldı.',
            'technologies': 'Django, PostgreSQL, Transformers, Python, HTML/CSS, JavaScript, REST API, LlaMA, Gemini, Pandas, NumPy, Requests, Aiohttp, Asyncio, BeautifulSoup, Selenium, Playwright',
            'about_html': load_content_file('sinavizcisi_about.html'),
            'project_info': {
                'category': 'Web Geliştirme, Veri Analizi, Yapay Zeka, Web Scraping',
                'status': 'aktif',
                'start_date': '2025-06',
            },
            'features': [
                {'title': 'Gerçek Veriye Dayalı', 'description': '100.000+ sayfa görüntülenmesi ve resmi istatistiklerle sürekli güncellenen içerikler.', 'icon': 'fas fa-database'},
                {'title': 'Üniversite & Bölüm Profilleri', 'description': 'Akademik kadro, burs, kampüs yaşamı ve şehir detaylarına kadar kapsamlı kılavuz.', 'icon': 'fas fa-university'},
                {'title': 'Lise Bazlı Özel Analizler', 'description': 'Her lisenin yıllara göre sıralama ortalamaları, en çok tercih ettiği bölümler ve yerleşme başarıları. Bu veriler başka hiçbir yerde yok.', 'icon': 'fas fa-school'},
                {'title': 'Detaylı İstatistikler', 'description': 'Kontenjan değişimleri, yıl bazlı trendler ve tercih istatistiklerini görselleştirilmiş panellerde sunar.', 'icon': 'fas fa-chart-bar'},
                {'title': 'Akıllı Karşılaştırmalar', 'description': 'Üniversite ve bölümleri yan yana kıyaslama ile karar sürecini kolaylaştırır.', 'icon': 'fas fa-columns'},
                {'title': 'Duygu Analizli Yorumlar', 'description': 'Öğrenci yorumlarını yapay zekâ ile pozitif, negatif veya nötr olarak sınıflandırır.', 'icon': 'fas fa-comments'}
            ],
            'technical_details': load_content_file('sinavizcisi_technical.html'),
            'readme_url': '',
            'github_link': '',
            'demo_link': 'https://sinavizcisi.com',
            'order': 1
        },
        {
            'title': 'YokAPI',
            'slug': 'yokapi',
            'description': "YÖK Atlas verilerini normalize eden ve tek API'de sunan veri katmanı. Asenkron yapıya sahip toplu hızlı veri çekme işlemleri için YÖK Atlas'ın yıllara göre dağınık ve farklılaşan site yapısını standardize edip JSON formatında sunan güçlü bir araç.",
            'technologies': 'Python, Requests, Aiohttp, Asyncio, Pydantic, OOP',
            'about_html': load_content_file('yokapi_about.html'),
            'project_info': {
                'category': 'API Geliştirme',
                'status': 'aktif',
                'start_date': '2025-03',
                'license': 'MIT'
            },
            'features': [
                {'title': 'Normalize Edilmiş Veri', 'description': 'Farklı kaynaklardan gelen YÖK Atlas verileri tek formatta sunulur.', 'icon': 'fas fa-database'},
                {'title': 'Kolay Entegrasyon', 'description': 'Basit REST endpointleri ve Python kütüphanesi ile hızlıca projelere entegre edilir.', 'icon': 'fas fa-plug'},
                {'title': 'Asenkron Destek', 'description': 'aiohttp ve asyncio ile yüksek performanslı, asenkron veri çekme desteği.', 'icon': 'fas fa-bolt'},
                {'title': 'Zengin Veri Modelleri', 'description': 'Pydantic tabanlı güçlü modeller ile güvenli ve tip kontrollü veri kullanımı.', 'icon': 'fas fa-project-diagram'},
                {'title': 'Gelişmiş Fonksiyonlar', 'description': 'Kontenjan, taban puan, tercih istatistikleri, lise ve il bazlı dağılımlar gibi onlarca fonksiyon.', 'icon': 'fas fa-chart-bar'},
                {'title': 'Esnek Session Kullanımı', 'description': 'Kendi aiohttp sessionunuzu kullanabilir veya otomatik oluşturulan session ile çalışabilirsiniz.', 'icon': 'fas fa-exchange-alt'},
            ],
            'technical_details': load_content_file('yokapi_technical.html'),
            'readme_url': 'https://github.com/izcir/YokAPI/blob/main/README.md',
            'github_link': 'https://github.com/izcir/YokAPI/',
            'demo_link': '',
            'order': 2
        },
        {
            'title': 'EBA Puan Botu',
            'slug': 'eba-puan-botu',
            'description': "EBA'da puan kasmayı sağlayan masaüstü arayüze sahip bir bot.",
            'technologies': 'Python, Selenium, PyQt5, Requests, BeautifulSoup, CSS, Threading',
            'about_html': load_content_file('eba_puan_botu_about.html'),
            'project_info': {
                'category': 'Masaüstü Uygulama',
                'start_date': '2020-03'
            },
            'features': [
                {'title': 'Otomatik Giriş', 'description': 'EBA hesabınıza güvenli şekilde otomatik giriş yaparak manual işlemi ortadan kaldırır.', 'icon': 'fas fa-sign-in-alt'},
                {'title': 'Toplu Veri Çekme', 'description': 'Tüm puanlar ve içerik verilerinizi tek seferde toplayarak zaman kazandırır.', 'icon': 'fas fa-download'},
                {'title': 'Esnek Export', 'description': 'Verilerinizi CSV ve JSON formatlarında export ederek farklı uygulamalarda kullanım sağlar.', 'icon': 'fas fa-file-export'},
                {'title': 'Kullanıcı Dostu Arayüz', 'description': 'PyQt5 ile tasarlanmış sezgisel masaüstü arayüzü ile kolay kullanım.', 'icon': 'fas fa-desktop'},
                {'title': 'İlerleme Takibi', 'description': 'Real-time progress bar ile işlem durumunu takip edebilirsiniz.', 'icon': 'fas fa-tasks'},
                {'title': 'Threading Desteği', 'description': 'Arka planda çalışan işlemler sayesinde arayüz donmadan kullanım.', 'icon': 'fas fa-cogs'},
            ],
            'technical_details': load_content_file('eba_puan_botu_technical.html'),
            'readme_url': 'https://github.com/izcir/EbaPuanBot/blob/main/README.md',
            'github_link': 'https://github.com/izcir/EbaPuanBot',
            'demo_link': '',
            'order': 3
        }
    ]
    
    for project_data in projects_data:
        project = Project.objects.create(**project_data)
        print(f"✓ {project.title} oluşturuldu")
    
    print(f"Toplam {len(projects_data)} proje oluşturuldu.")

def create_skills():
    skills_data = [
        {
            'name': 'Python',
            'description': 'Uzun süredir Python ile çalışıyorum ve bu dilde kendime oldukça güveniyorum. Nesne yönelimli programlama ve asenkron programlama konularında deneyimliyim. Requests, Aiohttp, Asyncio, BeautifulSoup, Selenium, Playwright, Django, SQLAlchemy, Pandas, NumPy gibi kütüphanelerle çeşitli projeler geliştirdim. SQLite ve PostgreSQL ile veritabanı yönetimi tecrübem var.',
            'level': 'advanced',
            'icon': 'fab fa-python',
            'order': 1
        },
        {
            'name': 'Web Scraping',
            'description': 'Requests, BeautifulSoup, Selenium, Playwright ile bot korumalı sitelerden veri çekme, login/cookie işlemleri, toplu veri çekme ve proxy değiştirme konularında deneyim.',
            'level': 'advanced',
            'icon': 'fas fa-spider',
            'order': 2
        },
        {
            'name': 'Veri Analizi',
            'description': 'Pandas ve NumPy ile veri temizleme, analiz ve büyük veri setleriyle çalışma tecrübesi.',
            'level': 'intermediate',
            'icon': 'fas fa-chart-bar',
            'order': 3
        },
        {
            'name': 'Django',
            'description': 'İleri seviye Django web geliştirme, ölçeklenebilir sistemler ve veritabanı optimizasyonu. sinavizcisi.com platformunun tüm veritabanı ve backend mimarisini Django ile tasarladım.',
            'level': 'advanced',
            'icon': 'fab fa-django',
            'order': 4
        },
        {
            'name': 'PostgreSQL',
            'description': 'sinavizcisi.com’un veritabanı tasarımını PostgreSQL ile yaptım. Büyük ölçekli veri tabanlarıyla çalışma, performans ve optimizasyon.',
            'level': 'intermediate',
            'icon': 'fas fa-database',
            'order': 5
        },
        {
            'name': 'PyQt5',
            'description': 'Masaüstü uygulama geliştirme, özel CSS tasarımları ile kullanıcı arayüzü.',
            'level': 'intermediate',
            'icon': 'fas fa-desktop',
            'order': 6
        },
        {
            'name': 'Frontend',
            'description': 'HTML, CSS, JavaScript temel seviyede, üretime yeterli frontend geliştirme. Arayüz tasarımında yapay zekâ destekli araçlar ve hazır tasarımlardan faydalanıyorum. sinavizcisi.com ve bu bireysel portföy sitesi için temel frontend kodlarını ben yazdım.',
            'level': 'beginner',
            'icon': 'fas fa-code',
            'order': 7
        },
        {
            'name': 'Yapay Zeka',
            'description': 'Transformers, makine öğrenmesi modelleri ve veri odaklı AI çözümleri. sinavizcisi.com’da BERT ve LLaMA ile duygu analizi ve metin sınıflandırma.',
            'level': 'intermediate',
            'icon': 'fas fa-brain',
            'order': 8
        },
        {
            'name': 'SQLite',
            'description': 'Küçük ve orta ölçekli projelerde hızlı ve pratik veritabanı çözümleri için SQLite kullanıyorum.',
            'level': 'intermediate',
            'icon': 'fas fa-database',
            'order': 9
        },
        {
            'name': 'C & Ruby',
            'description': 'Üniversite dersleri kapsamında temel seviyede C ve Ruby ile çalışma tecrübesi.',
            'level': 'beginner',
            'icon': 'fas fa-terminal',
            'order': 10
        }
    ]
    print("Yetenekler ekleniyor...")
    for skill_data in skills_data:
        Skill.objects.create(**skill_data)
    print("Yetenekler eklendi.")

def main():
    """Ana fonksiyon"""
    print("=== Ramazan İzci Portföy Sitesi - Veri Yükleme ===")
    print()
    
    # Önce mevcut verileri temizle
    clear_data()
    print()
    
    # Projeleri oluştur
    create_projects()
    print()
    
    # Yetenekleri oluştur
    create_skills()
    print()
    
    print("=== Veri yükleme tamamlandı! ===")
    print()
    print("Şimdi aşağıdaki komutla sunucuyu başlatabilirsiniz:")
    print("python manage.py runserver")
    print()
    print("Admin paneline erişmek için:")
    print("http://127.0.0.1:8000/" + os.environ.get('ADMIN_URL', 'admin/'))

if __name__ == '__main__':
    main()
