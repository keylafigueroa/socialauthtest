from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import redirect_to
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^login/$', redirect_to, {'url':'/login/twitter'}),
    url(r'^private/$', 'espe_app.views.privado', name='privado'),
    url(r'^$', 'espe_app.views.home', name='home'),
    # url(r'^espe/', include('espe.foo.urls')),
    url(r'^api/Alumno/$', 'espe_app.views.consultar_alumno_api', name='consultar_alumno'),
    url(r'^api/Noticia/$', 'espe_app.views.consultar_noticias_api', name='consultar_noticias'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)

urlpatterns += patterns('django.views.static',
    (r'^static/(?P<path>.*)$', 'serve',
     {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)