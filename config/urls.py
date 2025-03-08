# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # home
    path('', include('home.urls', namespace='home')),
    # movies
    path('', include('movies.urls', namespace='movies')),
    # accounts
    path('', include('accounts.urls', namespace='accounts')),
    # admin
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)