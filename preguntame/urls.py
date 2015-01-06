from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomePageView

urlpatterns = patterns('',
    
    url(r'^$', HomePageView.as_view(), name='home'),
   
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^preguntas/', include('askme.urls', namespace="askme")),

    url(r'^admin/', include(admin.site.urls)),
)
