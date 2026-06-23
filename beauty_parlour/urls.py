from django.contrib import admin
from django.urls import path
from beauty_parlour import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('price', views.price, name='price'),
    path('team', views.team, name='team'),
    path('gallery', views.gallery, name='gallery'), 
    path('contact', views.contact, name='contact'), 
    path('home', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
