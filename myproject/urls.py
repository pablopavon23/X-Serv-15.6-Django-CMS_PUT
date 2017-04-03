from django.conf.urls import include, url
from django.contrib import admin
from cms_put import views

urlpatterns = [
    url(r'^$', views.barra, name='barra'),
    url(r'^pagina/(\d+)$', views.pagina, name='bebida'),
    url(r'^admin/', include(admin.site.urls)),
]
