from django.db import models
from datetime import datetime

# Create your models here.
class Auction(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50, default='Anonymous')
    description = models.CharField(max_length=100, blank=True)
    background_color = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=32, default='Anonymous')
    image = models.ImageField(upload_to='static/images')
    original_image = models.ImageField(upload_to='static/images', blank=True)
    end_date = models.DateTimeField('end date(UTC)', default=datetime.now, blank=False)
    auction = models.ForeignKey(Auction, default=None)

    @property
    def is_expired(self):
        end = datetime(self.end_date.year, self.end_date.month, self.end_date.day, hour=self.end_date.hour, minute=self.end_date.minute)
        return datetime.now() >= end

    def __str__(self):
        return self.name

class Bid(models.Model):
    artwork = models.ForeignKey(Product)
    name = models.CharField(max_length=32, default='Anonymous')
    email = models.EmailField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    bid_date = models.DateField('bid date', auto_now_add=True)

    def __str__(self):
        return self.name
