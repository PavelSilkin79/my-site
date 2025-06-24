from django.shortcuts import render
from django.utils.timezone import now
from .models import About, Service, Contact, GalleryImage, CompanyCard, ContactBackground

def index(request):
    about = About.objects.first()
    services = Service.objects.all()
    gallery = GalleryImage.objects.all()
    return render(request, 'main/index.html', {
        'about': about,
        'services': services,
        'gallery': gallery,
        'now': now(),
    })


def contacts_view(request):
    contact = Contact.objects.first()
    company_card = CompanyCard.objects.first()
    background = ContactBackground.objects.last()
    return render(request, 'main/contacts.html', {
        'contact': contact,
        'company_card': company_card,
        'background': background,
    })
