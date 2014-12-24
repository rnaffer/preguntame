from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
	url(r'^preguntas/', include('askme.urls', namespace="preguntas")),
	url(r'^cuentas/', include('cuentas.urls', namespace="cuentas")),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
