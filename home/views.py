from django.shortcuts import render, redirect
from django.db.models import Max
from .models import Artwork, Bid
from . import validation

# Create your views here.
def list_artwork(request):
    context = dict()

    #Get max bid amount of each art
    bids = []
    artwork = Artwork.objects.all()
    for art in artwork:
        max_bid = art.bid_set.all().aggregate(Max('amount'))['amount__max']
        if max_bid != None:
            bids.append('Highest bid: $'+str(max_bid))
        else:
            bids.append('There are no bids at this time')

    context['pkg'] = zip(artwork, bids)
    return render(request, 'list_artwork.html', context)

# includes bidding
def view_artwork(request, item_id):

    context = dict()
    context['item_id'] = item_id
    context['item'] = Artwork.objects.get(id=item_id)
    context['bidders'] = Bid.objects.all().filter(artwork__id=item_id).order_by('-amount')

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        amount = request.POST['amount']

        valid = validation.validate(name, email, amount, context['item'])

        if valid == validation.VALID:
            bid = Bid(artwork=Artwork.objects.get(id=item_id), name=name, email=email, amount=amount)
            bid.save()
            return redirect('view_artwork', item_id)
        elif valid == validation.LOW_BID:
            context['error_message'] = 'Your bid must be at least $1 greater than the current highest bid'
            return render(request, 'view_artwork.html', context)
        elif valid == validation.INVALID:
            context['error_message'] = 'You have entered an invalid entry. Please make sure that all fields are filled appropriately'
            return render(request, 'view_artwork.html', context)

    return render(request, 'view_artwork.html', context)
