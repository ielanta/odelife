from django.core.exceptions import ValidationError

LIMIT_TAGS = 5


def validate_tags(value):
    if len(value) > LIMIT_TAGS:
        raise ValidationError("Максимальное число тегов: %d" % LIMIT_TAGS)
