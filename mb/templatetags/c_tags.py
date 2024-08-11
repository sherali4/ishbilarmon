from django import template
from mb.models import Category, Malumot


register = template.Library()

# @register.simple_tag()
# @register.simple_tag(name='get_list_categories')
# def get_categories():
#     return Category.objects.all()
@register.inclusion_tag('tags/siat_c.html')
def categories():
    ct = Category.objects.all()
    return { "ct": ct }