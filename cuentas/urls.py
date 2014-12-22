from django.conf.urls import patterns, include, url

from cuentas import views

urlpatterns = patterns('',

	url(r'^registro/$', views.AccountRegistrationView.as_view(), name='registro'),
	url(r'^login/$', views.LoginFormView.as_view(), name='login'),
	url(r'^logout/$', 'cuentas.views.logout_view', name="logout"),
)