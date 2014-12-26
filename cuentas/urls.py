from django.conf.urls import patterns, include, url
from cuentas import views
from cuentas.decorator import anonymous_required

urlpatterns = patterns('',

	url(r'^login/', anonymous_required(views.LoginFormView.as_view()), name='login'),
	url(r'^registro/$', anonymous_required(views.AccountRegistrationView.as_view()), name='registro'),
	#url(r'^login/$', views.LoginFormView.as_view(), name='login'),
	url(r'^logout/$', 'cuentas.views.logout_view', name="logout"),
)