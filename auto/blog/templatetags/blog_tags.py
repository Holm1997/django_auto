from django import template
from blog.models import *

register = template.Library()



@register.inclusion_tag('blog/list_brands.html')
def show_brands(sort=None, brands_selected=0):
    if not sort:
        brands = Brand.objects.all()
    else:
        brands = Brand.objects.order_by(sort)

    return {'brands': brands, 'brands_selected': brands_selected}