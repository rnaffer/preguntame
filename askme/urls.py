from django.conf.urls import patterns, include, url

from .views import (AskListView, AskDetailList,
 CategoryView, VoteUpView, VoteDownView, AskCreateView)

urlpatterns = patterns(
	'',
	url(r'^$', AskListView.as_view(), name='asks'),
	url(r'^crear/$', AskCreateView.as_view(), name='create'),
	url(r'^c/(?P<slug>[-\w]+)/$', CategoryView.as_view(),
	 name='category'),
	url(r'^d/(?P<slug>[-\w]+)/$', AskDetailList.as_view(),
	 name='detail'),
	url(r'^plus/(?P<pk>\d+)/$', VoteUpView.as_view(),
	 name='plus'),
	url(r'^minus/(?P<pk>\d+)/$', VoteDownView.as_view(),
	 name='minus'),

)