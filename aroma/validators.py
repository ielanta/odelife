from django.core.exceptions import ValidationError

LIMIT_NOTES = 1


def validate_notes(value):
    if len(value) > LIMIT_NOTES:
        raise ValidationError("Максимальное число нот для поиска: %d" % LIMIT_NOTES)
