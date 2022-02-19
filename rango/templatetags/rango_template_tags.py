from django import template
from rango.models import Category
from django.contrib.auth.models import User
register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category = None):
 return {'categories': Category.objects.all(), "current_category" : current_category}