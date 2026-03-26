from django.db import models

# Every model list here, whene we run the migration coommand,
# Create your models here.
class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Carousel - {self.title.capitalize()}"