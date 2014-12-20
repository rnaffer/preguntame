from django.conf.urls import patterns, include, url
from django.contrib import admin

from askme import views

urlpatterns = patterns('',
    # Examples:
	url(r'^preguntas/', include('askme.urls', namespace="preguntas")),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
