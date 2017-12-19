from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from blog.views import index, upload, gallery, about, wmarked, gal


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^upload/$', upload, name='upload'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^sample/$', gal, name='sample'),
    url(r'^wmarked/$', wmarked, name='wmarked'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

