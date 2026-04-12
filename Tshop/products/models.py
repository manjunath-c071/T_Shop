from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"Category : {self.title.capitalize()}"

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Brand : {self.name}"


class Product(models.Model):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    desc = models.TextField(max_length=500)
    thumbnail = models.ImageField(upload_to='products/thumbnails/')
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        brand_name = self.brand.name if self.brand else 'No Brand'
        return f"{self.title} ({brand_name})"


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/images/')
    caption = models.CharField(max_length=50)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return f"{self.caption} — {self.product.title}"