from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.main.views import index, contacts_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', views.contacts_view, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
