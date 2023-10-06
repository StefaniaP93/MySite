from django.db import models
from PIL import Image
from django.core.files import File
from io import BytesIO

class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default='')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    carousel = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)


    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return self.slug

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
