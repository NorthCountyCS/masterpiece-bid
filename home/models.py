from django.db import models
from datetime import datetime

# Create your models here.
class Artwork(models.Model):
    name = models.CharField(max_length=32)
    artist = models.CharField(max_length=32, default='Anonymous')
    image = models.ImageField(upload_to='static/images')
    original_image = models.ImageField(upload_to='static/images', blank=True)
    pub_date = models.DateField('date published', auto_now_add=True)
    end_date = models.DateField('end date')

    @property
    def is_expired(self):
        end = datetime(self.end_date.year, self.end_date.month, self.end_date.day, hour=14, minute=15)
        if datetime.now() >= end:
            return True
        return False

    def __str__(self):
        return self.name

class Bid(models.Model):
    artwork = models.ForeignKey(Artwork)
    name = models.CharField(max_length=32, default='Anonymous')
    email = models.EmailField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    bid_date = models.DateField('bid date', auto_now_add=True)

    def __str__(self):
        return self.name
