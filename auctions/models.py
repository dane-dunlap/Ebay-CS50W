from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    

#need to add watchlist to users
#need to add category
#need to make sure that a listing is associated with a user

class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category_name}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField (max_length = 350)
    image = models.URLField(max_length = 200,blank=True)
    active = models.BooleanField(default=True)
    starting_bid = models.IntegerField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name="category")
    watchlist = models.ManyToManyField(User,blank=True,null=True,related_name="watchlist_listing")

    
    def __str__(self):
        return f"{self.id}: {self.title}"


    
class Bid(models.Model):
    bid_amount = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Comment (models.Model):
    comment = models.CharField (max_length = 350)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    


