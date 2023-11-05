from django import template

register = template.Library()

@register.simple_tag
def media_path(val):
    return f'/media/{val}'