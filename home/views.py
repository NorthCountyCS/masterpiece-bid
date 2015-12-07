from django.shortcuts import render, redirect
from .models import Artwork, Bid
from django.db.models import Max
from . import validation

# Create your views here.
def list_artwork(request):
    context = dict()

    #Get max bid amount of each art
    bids = []
    artwork = Artwork.objects.all()
    for art in artwork:
        bids.append(art.bid_set.all().aggregate(Max('amount'))['amount__max'])

    context['pkg'] = zip(artwork, bids)
    return render(request, 'list_artwork.html', context)

# includes bidding
def view_artwork(request, item_id):

    context = dict()
    context['item_id'] = item_id
    context['item'] = Artwork.objects.get(id=item_id)
    context['bidders'] = Bid.objects.all().filter(artwork__id=item_id).order_by('-amount')

    if request.method == 'POST':

        email = request.POST['email']
        amount = request.POST['amount']

        if validation.validate(email,amount):
            bid = Bid(artwork=Artwork.objects.get(id=item_id), email=email, amount=amount)
            bid.save()
            return redirect('view_artwork', item_id)
        else:
            context['error_message'] = 'That dun work'
            return render(request, 'view_artwork.html', context)

    return render(request, 'view_artwork.html', context)

