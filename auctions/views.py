from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User,Listing,Bid,Comment, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import User


def index(request):
    listings =Listing.objects.all()
    return render(request, "auctions/index.html",{"listings":listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    categories = Category.objects.all()
    if request.method =="POST":
        current_user = request.user
        title = request.POST['title']
        description = request.POST['description']
        image = request.POST['image']
        starting_bid = request.POST['starting_bid']
        new_listing = Listing(title = title,description = description,image=image,starting_bid=starting_bid,creator=current_user)
        new_listing.save()
        
        
        return render(request,"auctions/index.html",)

    else:
        return render(request,"auctions/create.html",{"categories":categories})



def listing(request,listing_id):
    if request.method == "GET":
        listing = Listing.objects.get(id=listing_id)
        highest_bid = (Bid.objects.filter(listing=listing)).aggregate(Max('bid_amount'))
        current_user = request.user
        creator = listing.creator
        if current_user == creator:
            listing_owner = True
        else:
            listing_owner = False
        return render(request,"auctions/listing.html",{
            "listing":listing,"highest_bid":highest_bid['bid_amount__max'],"listing_owner":listing_owner
        })

@login_required
def place_bid(request,listing_id):
    bid = int(request.POST['bid'])
    listing = Listing.objects.get(id=listing_id)
    highest_bid = (Bid.objects.filter(listing=listing)).aggregate(Max('bid_amount'))
    if bid > highest_bid['bid_amount__max']:
        new_bid = Bid(bid_amount=bid,listing=listing)
        new_bid.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        message = "Bid must be greater than the highest bid"
        return render(request,"auctions/listing.html",{"listing":listing,"message":message,"highest_bid":highest_bid["bid_amount__max"]})




        