from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    
    #url(r'^$', HomePageView.as_view(), name='home'),
   
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^preguntas/', include('askme.urls', namespace="askme")),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))