from django.db import models

# Create your models here.
class Artwork(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='images')
    pub_date = models.DateField('date published', auto_now_add=True)
    end_date = models.DateField('date ends')

    def __str__(self):
        return self.name

class Bid(models.Model):
    artwork = models.ForeignKey(Artwork)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    bid_date = models.DateField('bid date', auto_now_add=True)

    def __str__(self):
        return self.email