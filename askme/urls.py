from django.conf.urls import patterns, include, url

from askme import views

urlpatterns = patterns('',

	url(r'^$', views.PreguntaListView.as_view(), name='preguntas'),
	url(r'^categoria/(\d+)$', 'askme.views.categoria', name='categoria'),
	#url(r'^/page(?P<page>[0-9]+)/$', 'object_list', dict(info_dict)),
	url(r'^(?P<pk>\d+)/$', views.PreguntaDetailView.as_view(), name='detalle'),
	url(r'^plus/(\d+)$', 'askme.views.plus', name='plus'),
	url(r'^minus/(\d+)$', 'askme.views.minus', name='minus'),
	url(r'^preguntame/$', views.PreguntameFormView.as_view(), name='preguntame'),

    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^preguntas/$', PreguntaListView.as_view(), name='preguntas'),
)
