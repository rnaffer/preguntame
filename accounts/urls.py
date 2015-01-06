from django.conf.urls import patterns, include, url

from .views import SignUpView, LogInView, LogOutView

urlpatterns = patterns(
	'',
    url(r'^register/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', LogInView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
)