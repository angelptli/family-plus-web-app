from django import template

register = template.Library()

@register.simple_tag
def get_verbose_field(instance, field_name):
    """Return the object's verbose name."""
    # Credit https://stackoverflow.com/questions/14496978/fields-verbose-name-in-templates
    return instance._meta.get_field(field_name).verbose_name
