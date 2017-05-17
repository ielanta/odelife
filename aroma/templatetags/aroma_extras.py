from django import template
from django.template import TemplateSyntaxError
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def notes_in_category(notes, category):
    print(notes, category)
    return notes.filter(categorynotes__category=category)


@register.filter
def notes_in_category_exists(notes, category):
    print(notes, category)
    return notes.filter(categorynotes__category=category).exists()


@register.filter(is_safe=False)
@stringfilter
# {{ val|ru_pluralize: 'аромат', 'аромата', 'ароматов' }}
def ru_pluralize(n, str1, str2, str3):
    try:
        return str1 if n % 10 == 1 & n % 100 != 11 else str2 if n % 10 >= 2 & n % 10 <= 4 & (
            n % 100 < 10 | n % 100 >= 20) else str3
    except:
        raise TemplateSyntaxError


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
