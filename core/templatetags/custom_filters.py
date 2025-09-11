from django import template

register = template.Library()

@register.filter
def split(value, delimiter):
    return value.split(delimiter)

@register.filter  
def trim(value):
    return value.strip() if value else value

@register.filter
def mul(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0
