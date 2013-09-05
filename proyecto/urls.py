from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^hola/$', 'app.views.hola', name='hola'),
    url(r'^numero/(\d+)$', 'app.views.numero', name='numero'),
    url(r'^plantilla/$', 'app.views.plantilla', name='plantilla'),
    url(r'^masdatos/$', 'app.views.masdatos', name='masdatos'),
    # url(r'^proyecto/', include('proyecto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
