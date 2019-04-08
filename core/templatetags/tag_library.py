from django import template

register  = template.Library()

# With this filter you can return a string number into a integer
@register.filter()
def to_int(value):
    return int(value)