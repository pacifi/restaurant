
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sobre/$','myapp.views.sobre', name='sobre'),
    url(r'^bebidas/$','myapp.views.lista_bebidas'),
    url(r'^$','myapp.views.inicio', name='inicio'),
    url(r'^recetas/$','myapp.views.lista_recetas', name='lista_rece'),
    url(r'^receta/(?P<id_receta>\d+)$','myapp.views.detalle_receta'),
    url(r'^receta/nueva/$','myapp.views.nueva_receta'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
