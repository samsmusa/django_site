from django import template

register = template.Library()


@register.filter
def to_class_name(value):
    return value.__class__.__name__


@register.filter
def split(value):
  """
    Returns the value turned into a list.
  """
  return str(value).split('-')
  
  
  
  
@register.filter(is_safe=True)
def regularStar(value, arg):
    """Removes all values of arg from the given string"""
    return abs(value-int(arg))*'a'