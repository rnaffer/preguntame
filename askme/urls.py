from django.conf.urls import patterns, include, url

from askme import views

urlpatterns = patterns('',
    url(r'^$', views.PreguntaListView.as_view(), name='preguntas'),
	url(r'^(?P<pk>\d+)/$', views.PreguntaDetailView.as_view(), name='detalle'),

    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^preguntas/$', PreguntaListView.as_view(), name='preguntas'),
)
