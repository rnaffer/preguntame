from django.conf.urls import patterns, include, url
from django.conf import settings

from .views import SignUpView, LogInView, LogOutView, ProfileView

urlpatterns = patterns(
	'',
    url(r'^register/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', LogInView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
    url(r'^profile/(?P<pk>\d+)/(?P<username>\w+)/$', ProfileView.as_view(),
	 name='profile'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))