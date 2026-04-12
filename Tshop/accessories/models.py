from django.db import models

# Create your models here.

class AccessoryCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Accessory Categories"


class Accessory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        AccessoryCategory,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    desc = models.TextField(max_length=500)
    thumbnail = models.ImageField(upload_to='accessories/thumbnails/')
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Accessories"