from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#need to add watchlist to users
#need to add category
#need to make sure that a listing is associated with a user



class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField (max_length = 350)
    image = models.URLField(max_length = 200,blank=True)
    active = models.BooleanField(default=True)
    starting_bid = models.IntegerField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    
    

class Bid(models.Model):
    bid_amount = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Comment (models.Model):
    comment = models.CharField (max_length = 350)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    


