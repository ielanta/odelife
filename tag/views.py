from dal import autocomplete
from tag.models import Tag


class TagsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Tag.objects.order_by('name').all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q.lower())
        return qs
