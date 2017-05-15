from django import template

register = template.Library()


@register.filter
def notes_in_category(notes, category):
    print(notes, category)
    return notes.filter(categorynotes__category=category)


@register.filter
def notes_in_category_exists(notes, category):
    print(notes, category)
    return notes.filter(categorynotes__category=category).exists()
