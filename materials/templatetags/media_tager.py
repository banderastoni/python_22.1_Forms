from django import template

register = template.Library()


@register.filter()
def media_tager(value):
    if value:
        return f'/media/{value}'
    return ''


@register.simple_tag()
def media_tager(value):
    if value:
        return f'/media/{value}'
    return ''
