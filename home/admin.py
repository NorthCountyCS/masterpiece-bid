from django.contrib import admin
from .models import Bid, Artwork

# Register your models here.
@admin.register(Bid)
class Bid(admin.ModelAdmin):
    list_display = ['name', 'email', 'artwork', 'amount']

@admin.register(Artwork)
class Artwork(admin.ModelAdmin):
    list_display = ['name', 'end_date']