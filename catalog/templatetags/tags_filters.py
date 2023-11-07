from django import template

register = template.Library()

@register.simple_tag
@register.filter()
def mediapath(data) -> str:
    return data.url if data else '#'

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()