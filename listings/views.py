from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from listings.models import Listing, ListingForm
from django.contrib.auth.decorators import login_required

# Simple function for all listings
def listings(request):
  listings = Listing.objects.all()
  c = {
    'listings': listings,
  }
  return render(request, "pages/listings/listings.html", c)

def view_listing(request, lid):
  listing = Listing.objects.get(pk = lid)
  c = {
    'listing': listing,
  }

  return render(request, "pages/listings/view_listing.html", c)

@login_required
def edit_listing(request, listingID):
  if request.method == 'POST':
    if listingID == 'N':
      form = ListingForm(request.POST)
    else:
      l = Listing.objects.get(pk=listingID)
      form = ListingForm(request.POST, instance=l)
    if form.is_valid():
      tmp = form.save(commit=False)
      tmp.owner = request.user
      tmp.save()
      return HttpResponseRedirect("/user/dashboard/")
  else:
    if listingID == 'N':
      form = ListingForm()
    else:
      l = Listing.objects.get(pk=listingID)
      if l.owner != request.user:
        raise Http404("You cannot edit that")
      form = ListingForm(instance=l)
  return render(request, "pages/listings/edit_listing.html", { 'form':form, })
    
    


# Create your views here.
