from django.db import models

class CarouselImage(models.Model):
    file = models.FileField(upload_to='carousel/', null=True, blank=True)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def is_video(self):
        return str(self.file).lower().endswith(('.mp4', '.webm', '.ogg'))

    def __str__(self):
        return f"Carousel - {self.title.capitalize()}"