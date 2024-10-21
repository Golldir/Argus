from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def center_def(value):
    if value:
        return "justify-content: center; text-align: center;"
    else:
        return ''


# @register.simple_tag
# def ie_special(value, center):
#     if center:
#         return str(float(value) - 1.8)
#     else:
#         return value


@register.simple_tag
def display_sensor_info(value, units, code, line_breaks):
    return mark_safe(f'{value} {"<br>" if line_breaks else ""} {units}')
    # return mark_safe(f'{code[-7:]} {"<br>" if line_breaks else ""} {units}')



# @register.simple_tag
# def image_url_converter(image_url):
#     img2 = image_url.replace('.png', '_ie.png')
#     print('123', image_url)
#     return img2
