from django import forms

from tag.models import TaggedItem
from aroma.models import Aroma


class TaggedItemCreateForm(forms.ModelForm):
    class Meta:
        model = TaggedItem
        fields = '__all__'

    aroma = forms.ModelChoiceField(queryset=Aroma.objects.filter(is_public=True).all())
