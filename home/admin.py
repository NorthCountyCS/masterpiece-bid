from django.contrib import admin
from .models import Bid, Product, Auction

# Register your models here.
@admin.register(Bid)
class Bid(admin.ModelAdmin):
    list_display = ['name', 'email', 'artwork', 'amount']

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'artwork_url']

    def artwork_url(self, obj):
        return '<a href="%s">%s</a>' % ('/' + str(obj.id), 'Click here to view')
    artwork_url.allow_tags = True
    artwork_url.short_description = 'Product URL'

@admin.register(Auction)
class Auction(admin.ModelAdmin):
    list_display = ['name', 'end_date', 'teacher', 'description']
