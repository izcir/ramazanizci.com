# Ramazan İzci - Kişisel Portföy Sitesi

![Portföy Önizlemesi](media/index_page_2.jfif)

Bu proje, Ramazan İzci'nin kişisel portfolyo web sitesi. Django framework'ü kullanılarak geliştirilmiş, modern ve responsive bir tasarıma sahip. Site, projeler, yetenekler ve iletişim bölümlerini içeriyor.

## Özellikler

- **Responsive Tasarım**: Mobil ve masaüstü cihazlarda mükemmel görünüm
- **Koyu/Açık Tema**: Kullanıcı tercihine göre tema değiştirme
- **Proje Galerisi**: Detaylı proje açıklamaları ve teknik bilgiler
- **SEO Dostu**: Arama motorları için optimize edilmiş meta etiketler
- **Animasyonlar**: Sayfa geçişlerinde ve öğelerde yumuşak animasyonlar
- **İletişim Formu**: Kullanıcıların mesaj gönderebilmesi

## Teknolojiler

- **Backend**: Django 5.2
- **Frontend**: HTML5, Tailwind CSS, JavaScript (ES6+)
- **Veritabanı**: SQLite
- **Diğer**: Font Awesome, Google Fonts

## Proje Yapısı

```
ramazanizci/
├── core/                # Ana uygulama
├── projects/            # Proje yönetimi
├── skills/              # Yetenek yönetimi
├── pages/               # Statik sayfalar
├── templates/           # HTML şablonları
├── static/              # Statik dosyalar CSS, JS...
├── media/               # Medya dosyaları (resimler, yüklemeler)
└── ramazanizci/         # Django ayarları
```

## Kurulum ve Çalıştırma

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edin. Bu siteyi kendi portfolyonuz için de kullanabilirsiniz - sadece içerikleri kendinize göre düzenleyin.

### 1. Gereksinimler

- Python 3.8 veya üzeri
- Git

### 2. Projeyi İndirin

```bash
git clone https://github.com/izcir/ramazanizci.com.git
cd ramazanizci
```

### 3. Sanal Ortam Oluşturun (Önerilir)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 4. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 5. Çevre Değişkenlerini Ayarlayın

`.env.example` dosyasını `.env` olarak kopyalayın:

```bash
cp .env.example .env
```

`.env` dosyasını düzenleyin ve gerekli değerleri girin:

```env
# Django Environment Variables
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
ADMIN_URL=admin/
```

### 6. Veritabanını Hazırlayın

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Örnek Verileri Yükleyin (İsteğe Bağlı)

```bash
python load_data.py
```

### 8. Sunucuyu Çalıştırın

```bash
python manage.py runserver
```


## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

Ramazan İzci - [ramazan.izcir@gmail.com](mailto:ramazan.izcir@gmail.com)

Proje Linki: [https://github.com/izcir/ramazanizci.com](https://github.com/izcir/ramazanizci.com)
