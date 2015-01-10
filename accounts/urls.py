from django.conf.urls import patterns, include, url

from .views import (SignUpView, LogInView,
	 	LogOutView, ProfileView, ProfileUpdateView, UsersView)

urlpatterns = patterns(
	'',
    url(r'^register/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', LogInView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
    url(r'^users/$', UsersView.as_view(), name='users'),
    url(r'^profile/(?P<pk>\d+)/(?P<username>\w+)/$', ProfileView.as_view(),
	 name='profile'),
    url(r'^update/(?P<pk>\d+)$', ProfileUpdateView.as_view(),
	 name='update'),
)
