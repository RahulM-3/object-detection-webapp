from django.db import models

# Create your models here.
class uploadimage(models.Model):
    image = models.ImageField()