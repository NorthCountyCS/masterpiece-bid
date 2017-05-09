from django.shortcuts import render, redirect
from django.db.models import Max
from django.contrib.auth.models import User
from .models import Product, Bid, Auction
from . import validation
import datetime

# Create your views here.
def list_auction(request):
    return render(request, 'main.html', {'auctions': Auction.objects.all()})

def list_artwork(request, query):
    context = dict()
    # Get max bid amount of each art
    bids = []
    auction = Auction.objects.filter(name=query)

    if not auction:
        redirect('list_auction')
    auction = auction.get(name=query)
    context['auction'] = auction
    artwork = Product.objects.filter(auction=auction)
    for art in artwork:
        max_bid = art.bid_set.all().aggregate(Max('amount'))['amount__max']
        if max_bid != None:
            bids.append('Highest bid: $'+str(max_bid))
        else:
            bids.append('There are no bids at this time')

    context['pkg'] = zip(artwork, bids)
    return render(request, 'list_artwork.html', context)

def view_artwork(request, item_id):
    context = dict()
    product = Product.objects.get(id=item_id)
    context['item_id'] = item_id
    context['item'] = product
    context['bidders'] = Bid.objects.all().filter(artwork__id=item_id).order_by('-amount')
    context['auction'] = Auction.objects.get(name=product.auction.name)
    if request.method == 'POST':

        if context['item'].is_expired:
            return redirect('view_artwork', item_id)

        name = request.POST['name']
        email = request.POST['email']
        amount = request.POST['amount']
        valid = validation.validate(name, email, amount, context['item'])

        if valid == validation.VALID:
            bid = Bid(artwork=Product.objects.get(id=item_id), name=name, email=email, amount=amount)
            bid.save()
            try:
                notification.send(to=email ,message=('Masterpiece: %s\nBidder: %s\nAmount: %s\nEmail: %s\n'%(context['item'].name, name,amount,email)))
            except:
                pass
            return redirect('view_artwork', item_id)
        elif valid == validation.ZERO:
            context['error_message'] = 'Your bid can\'t be $0.00'
        elif valid == validation.LOW_BID:
            context['error_message'] = 'Your bid must be at least $1 greater than the current highest bid'
        elif valid == validation.INVALID:
            context['error_message'] = 'You have entered an invalid entry. Please make sure that all fields are filled appropriately'

    return render(request, 'view_artwork.html', context)
