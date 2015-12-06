from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Artwork, Bid

# Create your views here.
def list_artwork(request):
    context = dict()
    context['items'] = Artwork.objects.all()
    return render(request, 'list_artwork.html', context)

# includes bidding
def view_artwork(request, item_id):
    if request.method == 'POST':
        bid = Bid(artwork=Artwork.objects.get(id=item_id), email=request.POST['email'], amount=request.POST['amount'])
        bid.save()
        return redirect('view_artwork', item_id)

    context = dict()
    context['item_id'] = item_id
    context['item'] = Artwork.objects.get(id=item_id)
    context['bidders'] = Bid.objects.all().filter(artwork__id=item_id).order_by('-amount')
    return render(request, 'view_artwork.html', context)