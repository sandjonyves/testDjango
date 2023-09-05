from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache


index = never_cache(TemplateView.as_view(template_name = '/home/sandjon/test/testdjango/build/index.html'))