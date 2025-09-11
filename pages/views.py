from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Contact

def contact(request):
    if request.method == 'POST':
        last_submission = request.session.get('last_contact_submission')
        if last_submission:
            last_time = timezone.datetime.fromisoformat(last_submission)
            if timezone.now() - last_time < timedelta(seconds=10):
                messages.error(request, 'Çok sık mesaj gönderiyorsunuz. Lütfen 10 saniye bekleyin.')
                return redirect('core:home')
        
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        website = request.POST.get('website', '').strip()
        
        if website:
            messages.error(request, 'Bot tespit edildi!')
            return redirect('core:home')
        
        suspicious_words = ['http://', 'https://', 'www.', '<script', 'javascript:', 'onclick', 'onload']
        for word in suspicious_words:
            if word.lower() in (name + email + subject + message).lower():
                messages.error(request, 'Şüpheli içerik tespit edildi!')
                return redirect('core:home')
        
        if not all([name, email, subject, message]):
            messages.error(request, 'Lütfen tüm alanları doldurun.')
            return redirect('core:home')
        
        if '@' not in email or '.' not in email or email.count('@') != 1:
            messages.error(request, 'Geçerli bir email adresi girin.')
            return redirect('core:home')
        
        if len(name) > 100:
            messages.error(request, 'İsim çok uzun.')
            return redirect('core:home')
        
        if len(subject) > 200:
            messages.error(request, 'Konu çok uzun.')
            return redirect('core:home')
        
        if len(message) > 1000:
            messages.error(request, 'Mesaj çok uzun (maksimum 1000 karakter).')
            return redirect('core:home')
        
        try:
            contact_msg = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            request.session['last_contact_submission'] = timezone.now().isoformat()
            
            messages.success(request, 'Mesajınız başarıyla kaydedildi!')
        except Exception as e:
            messages.error(request, 'Mesaj kaydedilirken bir hata oluştu. Lütfen tekrar deneyin.')
        
        return redirect('core:home')
    
    return render(request, 'pages/contact.html')
