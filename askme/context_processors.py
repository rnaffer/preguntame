from django.core.urlresolvers import reverse
from .models import Category


def menu(request):
	menu = {'menu': []}

	for c in Category.objects.all():
		menu['menu'].append(
			{
			'title': c.title, 
			'url': reverse('askme:category', args=[c.slug])
			})

	return menu