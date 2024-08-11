from django import template
from django.shortcuts import get_object_or_404
from mb.models import Malumot, Category

register = template.Library()

@register.inclusion_tag('tags/siat.html')
def show_categories(id):
    mt = Malumot.objects.filter(turi_id=id)
    cat = Category.objects.filter(pk = id).first()
    return {
        "mt": mt,
        'cat': cat.name
            }

@register.inclusion_tag('tags/siat_m.html')
def show_categories_m(id):
    mt = Malumot.objects.filter(raqami=id).first()
    mt = Malumot.objects.filter(turi_id=mt.turi_id)
    return {
        "mt": mt,



            }