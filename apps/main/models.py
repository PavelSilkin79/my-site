from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(verbose_name="Описание о нас")
    image = models.ImageField(upload_to='about/', blank=True, verbose_name="Фото")
    resume_text = models.TextField(verbose_name="Резюме / Биография", blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    map_url = models.URLField(blank=True)

    def __str__(self):
        return self.phone


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or f"Фото #{self.pk}"

class CompanyCard(models.Model):
    full_name = models.CharField("Полное наименование", max_length=255)
    short_name = models.CharField("Краткое наименование", max_length=255)
    registration_address = models.CharField("Адрес регистрации", max_length=255)
    actual_address = models.CharField("Фактический адрес", max_length=255)
    inn = models.CharField("ИНН", max_length=12)
    ogrn = models.CharField("ОГРН", max_length=15)
    activity = models.TextField("ОКВЭД")


    def __str__(self):
        return self.short_name

class ContactBackground(models.Model):
    image = models.ImageField(upload_to='backgrounds/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Фон от {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
