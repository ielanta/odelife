from django.contrib import admin
from .models import Aroma, Note, Nose, Brand, Group, CategoryNotes
from aroma.forms import AromaCreateForm


class AromaAdmin(admin.ModelAdmin):
    form = AromaCreateForm
    search_fields = ('title',)


class BrandAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class NoteAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class CategoryNotesAdmin(admin.ModelAdmin):
    search_fields = ('aroma__title',)

admin.site.register(Aroma, AromaAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Nose)
admin.site.register(Group)
admin.site.register(Brand, BrandAdmin)
admin.site.register(CategoryNotes, CategoryNotesAdmin)
