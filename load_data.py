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
            'title_en': 'Sinavizcisi',
            'slug': 'sinavizcisi-com',
            'description': 'YKS yerleşme verilerinin ve üniversite yorumlarının yapay zekâ ile analiz edilip kullanıcıya sunduğum web platformu.',
            'description_en': 'A web platform where I analyze YKS placement data and university reviews with AI and present them to students.',
            'technologies': 'Django, PostgreSQL, Transformers, Python, HTML/CSS, JavaScript, REST API, LlaMA, Gemini, Pandas, NumPy, Requests, Aiohttp, Asyncio, BeautifulSoup, Selenium, Playwright',
            'technologies_en': 'Django, PostgreSQL, Transformers, Python, HTML/CSS, JavaScript, REST API, LlaMA, Gemini, Pandas, NumPy, Requests, Aiohttp, Asyncio, BeautifulSoup, Selenium, Playwright',
            'about_html': load_content_file('sinavizcisi_about.html'),
            'about_html_en': load_content_file('sinavizcisi_about_en.html'),
            'project_info': {
                'category': 'Web Geliştirme, Veri Analizi, Yapay Zeka, Web Scraping',
                'start_date': '2025-06',
            },
            'project_info_en': {
                'category': 'Web Development, Data Analysis, Artificial Intelligence, Web Scraping',
                'start_date': '2025-06',
            },
            'features': [
                {'title': 'Gerçek Veriye Dayalı', 'description': 'İlk 2 ayda 100.000 üzeri sayfa görüntülenmesi ve resmi istatistiklerle sürekli güncellenen içerikler.', 'icon': 'fas fa-database'},
                {'title': 'Üniversite & Bölüm Profilleri', 'description': 'Akademik kadro, burs, kampüs yaşamı ve şehir detaylarına kadar kapsamlı kılavuz.', 'icon': 'fas fa-university'},
                {'title': 'Lise Bazlı Özel Analizler', 'description': 'Her lisenin yıllara göre sıralama ortalamaları, en çok tercih ettiği bölümler ve yerleşme başarıları. Bu veriler başka hiçbir yerde yok.', 'icon': 'fas fa-school'},
                {'title': 'Detaylı İstatistikler', 'description': 'Kontenjan değişimleri, yıl bazlı trendler ve tercih istatistiklerini görselleştirilmiş panellerde sunar.', 'icon': 'fas fa-chart-bar'},
                {'title': 'Akıllı Karşılaştırmalar', 'description': 'Üniversite ve bölümleri yan yana kıyaslama ile karar sürecini kolaylaştırır.', 'icon': 'fas fa-columns'},
                {'title': 'Duygu Analizli Yorumlar', 'description': 'Öğrenci yorumlarını yapay zekâ ile pozitif, negatif veya nötr olarak sınıflandırır.', 'icon': 'fas fa-comments'}
            ],
            'features_en': [
                {'title': 'Data-Driven', 'description': '100,000+ page views in the first two months and continuously updated content backed by official statistics.', 'icon': 'fas fa-database'},
                {'title': 'University & Department Profiles', 'description': 'Comprehensive guides covering faculty, scholarships, campus life, and city details.', 'icon': 'fas fa-university'},
                {'title': 'High School-Specific Analyses', 'description': 'Yearly ranking averages, most preferred departments, and placement success for each high school. These data are not available elsewhere.', 'icon': 'fas fa-school'},
                {'title': 'Detailed Statistics', 'description': 'Quota changes, yearly trends, and preference stats delivered via visual dashboards.', 'icon': 'fas fa-chart-bar'},
                {'title': 'Smart Comparisons', 'description': 'Side-by-side comparisons of universities and departments to simplify decisions.', 'icon': 'fas fa-columns'},
                {'title': 'Sentiment-Based Reviews', 'description': 'Classifies student reviews as positive, negative, or neutral using AI.', 'icon': 'fas fa-comments'}
            ],
            'technical_details': load_content_file('sinavizcisi_technical.html'),
            'technical_details_en': load_content_file('sinavizcisi_technical_en.html'),
            'readme_url': '',
            'github_link': '',
            'demo_link': 'https://sinavizcisi.com',
            'order': 1
        },
        {
            'title': 'YokAPI',
            'title_en': 'YokAPI',
            'slug': 'yokapi',
            'description': "YÖK Atlas verilerini normalize eden ve tek API'de sunan veri katmanı. Asenkron yapıya sahip toplu hızlı veri çekme işlemleri için YÖK Atlas'ın yıllara göre dağınık ve farklılaşan site yapısını standardize edip JSON formatında sunan güçlü bir araç.",
            'description_en': "A data layer that normalizes YOK Atlas data and serves it through a single API. It standardizes YOK Atlas's scattered, year-variant structure and delivers JSON for high-speed async bulk fetching.",
            'technologies': 'Python, Requests, Aiohttp, Asyncio, Pydantic, OOP',
            'technologies_en': 'Python, Requests, Aiohttp, Asyncio, Pydantic, OOP',
            'about_html': load_content_file('yokapi_about.html'),
            'about_html_en': load_content_file('yokapi_about_en.html'),
            'project_info': {
                'category': 'API Geliştirme',
                'status': 'aktif',
                'start_date': '2025-03',
                'license': 'MIT'
            },
            'project_info_en': {
                'category': 'API Development',
                'status': 'active',
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
            'features_en': [
                {'title': 'Normalized Data', 'description': 'YOK Atlas data from different sources is delivered in a single format.', 'icon': 'fas fa-database'},
                {'title': 'Easy Integration', 'description': 'Simple REST endpoints and a Python library enable quick integration.', 'icon': 'fas fa-plug'},
                {'title': 'Async Support', 'description': 'High-performance async data fetching with aiohttp and asyncio.', 'icon': 'fas fa-bolt'},
                {'title': 'Rich Data Models', 'description': 'Strong Pydantic models for safe, type-checked data usage.', 'icon': 'fas fa-project-diagram'},
                {'title': 'Advanced Functions', 'description': 'Dozens of functions such as quotas, base scores, preference stats, and city-level distributions.', 'icon': 'fas fa-chart-bar'},
                {'title': 'Flexible Session Usage', 'description': 'Use your own aiohttp session or the auto-generated session.', 'icon': 'fas fa-exchange-alt'},
            ],
            'technical_details': load_content_file('yokapi_technical.html'),
            'technical_details_en': load_content_file('yokapi_technical_en.html'),
            'readme_url': 'https://github.com/izcir/YokAPI/blob/main/README.md',
            'github_link': 'https://github.com/izcir/YokAPI/',
            'demo_link': '',
            'order': 2
        },
        {
            'title': 'EBA Puan Botu',
            'title_en': 'EBA Score Bot',
            'slug': 'eba-puan-botu',
            'description': "EBA'da puan kasmayı sağlayan masaüstü arayüze sahip bir bot.",
            'description_en': 'A desktop bot with a GUI that automates earning points on EBA.',
            'technologies': 'Python, Selenium, PyQt5, Requests, BeautifulSoup, CSS, Threading',
            'technologies_en': 'Python, Selenium, PyQt5, Requests, BeautifulSoup, CSS, Threading',
            'about_html': load_content_file('eba_puan_botu_about.html'),
            'about_html_en': load_content_file('eba_puan_botu_about_en.html'),
            'project_info': {
                'category': 'Masaüstü Uygulama',
                'start_date': '2020-03'
            },
            'project_info_en': {
                'category': 'Desktop Application',
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
            'features_en': [
                {'title': 'Auto Login', 'description': 'Automatically logs in to your EBA account to remove manual steps.', 'icon': 'fas fa-sign-in-alt'},
                {'title': 'Bulk Data Fetch', 'description': 'Collects all points and content data in one run to save time.', 'icon': 'fas fa-download'},
                {'title': 'Flexible Export', 'description': 'Exports data to CSV and JSON for use in other tools.', 'icon': 'fas fa-file-export'},
                {'title': 'User-Friendly UI', 'description': 'An intuitive desktop interface built with PyQt5.', 'icon': 'fas fa-desktop'},
                {'title': 'Progress Tracking', 'description': 'Track processing status with a real-time progress bar.', 'icon': 'fas fa-tasks'},
                {'title': 'Threading Support', 'description': 'Background tasks keep the UI responsive.', 'icon': 'fas fa-cogs'},
            ],
            'technical_details': load_content_file('eba_puan_botu_technical.html'),
            'technical_details_en': load_content_file('eba_puan_botu_technical_en.html'),
            'readme_url': 'https://github.com/izcir/EbaPuanBot/blob/main/README.md',
            'github_link': 'https://github.com/izcir/EbaPuanBot',
            'demo_link': '',
            'order': 3
        },
        {
            'title': 'Türkiye Üniversite Bölüm Verileri (2019–2024)',
            'title_en': 'Turkish University Department Data (2019-2024)',
            'slug': 'turkish-university-admissions-dataset',
            'description': 'YÖK Atlas ve ÖSYM kaynaklarından toplanan 2019–2024 lisans/önlisans verilerini temizleyip standardize ederek analize hazır hale getiren kapsamlı veri seti.',
            'description_en': 'A comprehensive dataset that cleans and standardizes 2019-2024 undergraduate and associate program data collected from YOK Atlas and OSYM.',
            'technologies': 'Python, Pandas, CSV, ETL, Data Cleaning, Normalization',
            'technologies_en': 'Python, Pandas, CSV, ETL, Data Cleaning, Normalization',
            'about_html': load_content_file('tuad_about.html'),
            'about_html_en': load_content_file('tuad_about_en.html'),
            'project_info': {
                'category': 'Dataset / Veri Seti',
                'start_date': '2025-09',
                'license': 'MIT'
            },
            'project_info_en': {
                'category': 'Dataset',
                'start_date': '2025-09',
                'license': 'MIT'
            },
            'features': [
                {'title': 'Normalize İlişkisel Yapı', 'description': 'Lookup ve köprü tablolarıyla veri tekrarını azaltan ilişkisel dosyalar.', 'icon': 'fas fa-sitemap'},
                {'title': 'Denormalize Hızlı EDA', 'description': 'Tek dosyada tüm bilgilerin bulunduğu all_in_one_denormalized.csv ile hızlı keşif.', 'icon': 'fas fa-table'},
                {'title': 'Kontroller', 'description': 'Kontenjan-yerleşen tutarlılığı, cinsiyet dağılımı, puan/sıra eksiklik desenleri raporlandı.', 'icon': 'fas fa-check-circle'},
                {'title': 'ETL Betikleri', 'description': 'Ham veriden normalize ve denormalize çıktılara giden açık betikler.', 'icon': 'fas fa-code'},
            ],
            'features_en': [
                {'title': 'Normalized Relational Structure', 'description': 'Relational files with lookup and bridge tables that reduce duplication.', 'icon': 'fas fa-sitemap'},
                {'title': 'Denormalized Fast EDA', 'description': 'Quick exploration with all_in_one_denormalized.csv containing all data in one file.', 'icon': 'fas fa-table'},
                {'title': 'Consistency Checks', 'description': 'Quota-enrolled consistency, gender distribution, and missing score/rank patterns are reported.', 'icon': 'fas fa-check-circle'},
                {'title': 'ETL Scripts', 'description': 'Open scripts that go from raw data to normalized and denormalized outputs.', 'icon': 'fas fa-code'},
            ],
            'technical_details': load_content_file('tuad_technical.html'),
            'technical_details_en': load_content_file('tuad_technical_en.html'),
            'readme_url': 'https://github.com/izcir/turkish-university-admissions-dataset#readme',
            'github_link': 'https://github.com/izcir/turkish-university-admissions-dataset',
            'demo_link': '',
            'order': 4
        },
    ]
    
    for project_data in projects_data:
        project = Project.objects.create(**project_data)
        print(f"✓ {project.title} oluşturuldu")
    
    print(f"Toplam {len(projects_data)} proje oluşturuldu.")

def create_skills():
    skills_data = [
        {
            'name': 'Python',
            'name_en': 'Python',
            'description': 'Uzun süredir Python ile çalışıyorum ve bu dilde kendime oldukça güveniyorum. Nesne yönelimli programlama ve asenkron programlama konularında deneyimliyim. Requests, Aiohttp, Asyncio, BeautifulSoup, Selenium, Playwright, Django, SQLAlchemy, Pandas, NumPy gibi kütüphanelerle çeşitli projeler geliştirdim. SQLite ve PostgreSQL ile veritabanı yönetimi tecrübem var.',
            'description_en': 'I have been working with Python for a long time and feel very confident in it. I am experienced in object-oriented and asynchronous programming. I have built projects with Requests, Aiohttp, Asyncio, BeautifulSoup, Selenium, Playwright, Django, SQLAlchemy, Pandas, and NumPy. I also have experience managing databases with SQLite and PostgreSQL.',
            'level': 'advanced',
            'icon': 'fab fa-python',
            'order': 1
        },
        {
            'name': 'Web Scraping',
            'name_en': 'Web Scraping',
            'description': 'Requests, BeautifulSoup, Selenium, Playwright ile bot korumalı sitelerden veri çekme, login/cookie işlemleri, toplu veri çekme ve proxy değiştirme konularında deneyim.',
            'description_en': 'Experience extracting data from bot-protected sites, handling login/cookies, bulk scraping, and proxy rotation using Requests, BeautifulSoup, Selenium, and Playwright.',
            'level': 'advanced',
            'icon': 'fas fa-spider',
            'order': 2
        },
        {
            'name': 'Veri Analizi',
            'name_en': 'Data Analysis',
            'description': 'Pandas ve NumPy ile veri temizleme, analiz ve büyük veri setleriyle çalışma tecrübesi.',
            'description_en': 'Experience with data cleaning, analysis, and large datasets using Pandas and NumPy.',
            'level': 'intermediate',
            'icon': 'fas fa-chart-bar',
            'order': 3
        },
        {
            'name': 'Tahmin Modelleme',
            'name_en': 'Predictive Modeling',
            'description': 'XGBoost ile regresyon ve sınıflandırma; K-Means gibi kümeleme modelleriyle segmentasyon çalışmaları.',
            'description_en': 'Regression and classification with XGBoost; segmentation using clustering models like K-Means.',
            'level': 'intermediate',
            'icon': 'fas fa-chart-line',
            'order': 4
        },
        {
            'name': 'Django',
            'name_en': 'Django',
            'description': 'İleri seviye Django web geliştirme, ölçeklenebilir sistemler ve veritabanı optimizasyonu. sinavizcisi.com platformunun tüm veritabanı ve backend mimarisini Django ile tasarladım.',
            'description_en': 'Advanced Django web development, scalable systems, and database optimization. I designed the entire database and backend architecture of sinavizcisi.com with Django.',
            'level': 'advanced',
            'icon': 'fab fa-django',
            'order': 5
        },
        {
            'name': 'PostgreSQL',
            'name_en': 'PostgreSQL',
            'description': 'sinavizcisi.com’un veritabanı tasarımını PostgreSQL ile yaptım. Büyük ölçekli veri tabanlarıyla çalışma, performans ve optimizasyon.',
            'description_en': 'I designed the sinavizcisi.com database with PostgreSQL. Experience with large-scale databases, performance, and optimization.',
            'level': 'intermediate',
            'icon': 'fas fa-database',
            'order': 6
        },
        {
            'name': 'PyQt5',
            'name_en': 'PyQt5',
            'description': 'Masaüstü uygulama geliştirme, özel CSS tasarımları ile kullanıcı arayüzü.',
            'description_en': 'Desktop application development with custom CSS-based UI design.',
            'level': 'intermediate',
            'icon': 'fas fa-desktop',
            'order': 7
        },
        {
            'name': 'Frontend',
            'name_en': 'Frontend',
            'description': 'HTML, CSS, JavaScript temel seviyede, üretime yeterli frontend geliştirme. Arayüz tasarımında yapay zekâ destekli araçlar ve hazır tasarımlardan faydalanıyorum. sinavizcisi.com ve bu bireysel portföy sitesi için temel frontend kodlarını ben yazdım.',
            'description_en': 'Production-ready frontend development at a basic level with HTML, CSS, and JavaScript. I use AI-assisted tools and ready-made designs for UI. I wrote the core frontend code for sinavizcisi.com and this portfolio site.',
            'level': 'beginner',
            'icon': 'fas fa-code',
            'order': 8
        },
        {
            'name': 'Yapay Zeka',
            'name_en': 'Artificial Intelligence',
            'description': 'Transformers, makine öğrenmesi modelleri ve veri odaklı AI çözümleri. sinavizcisi.com’da BERT ve LLaMA ile duygu analizi ve metin sınıflandırma.',
            'description_en': 'Transformers, machine learning models, and data-driven AI solutions. Sentiment analysis and text classification with BERT and LLaMA on sinavizcisi.com.',
            'level': 'intermediate',
            'icon': 'fas fa-brain',
            'order': 9
        },
        {
            'name': 'SQLite',
            'name_en': 'SQLite',
            'description': 'Küçük ve orta ölçekli projelerde hızlı ve pratik veritabanı çözümleri için SQLite kullanıyorum.',
            'description_en': 'I use SQLite for fast and practical database solutions in small to medium-sized projects.',
            'level': 'intermediate',
            'icon': 'fas fa-database',
            'order': 10
        },
        {
            'name': 'C & Ruby',
            'name_en': 'C & Ruby',
            'description': 'Üniversite dersleri kapsamında temel seviyede C ve Ruby ile çalışma tecrübesi.',
            'description_en': 'Basic experience with C and Ruby as part of university coursework.',
            'level': 'beginner',
            'icon': 'fas fa-terminal',
            'order': 11
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
