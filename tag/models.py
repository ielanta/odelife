from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    aroma = models.ForeignKey('aroma.Aroma', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s #%d' % (self.aroma.title, self.tag.name, self.content_type, self.object_id)


