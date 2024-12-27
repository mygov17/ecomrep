from django import template

register = template.Library()

@register.filter
def hide_navbar(url_name):
    return url_name in ['login', 'register']
