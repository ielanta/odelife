from django.db import models


class Interaction(models.Model):
    aroma = models.ForeignKey('aroma.Aroma', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    link = models.URLField()
    item_id = models.IntegerField()
    partner_id = models.SmallIntegerField(default=1)
    name = models.CharField(max_length=200)
