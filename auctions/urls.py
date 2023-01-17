from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create",views.create,name="create"),
    path("listing/<int:listing_id>",views.listing,name="listing"),
    path("<int:listing_id>/place_bid",views.place_bid,name="place_bid"),
    path("<int:listing_id>/remove_listing",views.remove_listing,name="remove_listing"),
    path("categories",views.categories,name="categories"),
    path("<int:category_id>",views.category,name="category"),
    path("<int:listing_id>/add_to_watchlist",views.add_to_watchlist,name="add_to_watchlist"),
    path("<int:listing_id>/remove_from_watchlist",views.remove_from_watchlist,name="remove_from_watchlist"),
    path("watchlist",views.watchlist,name="watchlist")



]
