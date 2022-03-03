from django.shortcuts import render
from Auction.models import Listing

def index_view(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'auction/index.html', context = context)