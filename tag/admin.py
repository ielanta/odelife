from django.contrib import admin

from tag.models import Tag, TaggedItem
from tag.forms import TaggedItemCreateForm


class TaggedItemAdmin(admin.ModelAdmin):
    form = TaggedItemCreateForm


admin.site.register(Tag)
admin.site.register(TaggedItem, TaggedItemAdmin)
