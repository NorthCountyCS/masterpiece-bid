from django.contrib import admin
from .models import Bid, Artwork

# Register your models here.
@admin.register(Bid)
class Bid(admin.ModelAdmin):
    pass

@admin.register(Artwork)
class Artwork(admin.ModelAdmin):
    pass