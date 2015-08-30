
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sobre/$','myapp.views.sobre'),
    url(r'^bebidas/$','myapp.views.lista_bebidas'),
    url(r'^$','myapp.views.inicio'),
]
