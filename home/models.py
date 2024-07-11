from django.db import models

# Create your models here.
class Turf(models.Model):
    turf_name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.FloatField()
    turf_image = models.ImageField(upload_to ='static/image')
    start = models.IntegerField()
    end = models.IntegerField()
    turf_size = models.CharField(max_length=40)
    
    def __str__(self):
        return self.turf_name