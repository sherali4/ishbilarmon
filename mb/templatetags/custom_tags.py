from django import template
import datetime
register = template.Library()

@register.simple_tag
def format_date(value, format_string='%Y-%m-%d'):
    return value.strftime(format_string)