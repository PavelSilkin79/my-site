from django.contrib import admin
from .models import About, Service, Contact, GalleryImage, CompanyCard, ContactBackground


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'text', 'resume_text', 'image')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'map_url')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'caption', 'uploaded_at')
    ordering = ('-uploaded_at',)
    search_fields = ('caption',)


@admin.register(CompanyCard)
class CompanyCardAdmin(admin.ModelAdmin):
    list_display = ("short_name", "inn", "ogrn")

@admin.register(ContactBackground)
class ContactBackgroundAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at',)