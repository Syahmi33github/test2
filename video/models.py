from django.db import models
from django.utils.text import slugify


class PostModel(models.Model):
    judul = models.CharField(max_length=255)
    ahem = models.CharField(max_length=255, default="aa")
    bhem = models.CharField(max_length=255, default="ba")
    

    def save(self, *args, **kwargs):
        super(PostModel, self).save(*args, **kwargs)

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)
    
