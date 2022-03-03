from django.contrib import admin
from .models import User, Comment, Bid, Listing, Category



class ListingAdmin(admin.ModelAdmin):
    model = Listing
    list_display = ['id','title', 'starting_price', 'user', 'created_at', 'current_bid', 'is_active']

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['listing' ,'user', 'content']

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id','username', 'email']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id','name']

class BidAdmin(admin.ModelAdmin):
    model = Bid
    list_display = ['id', 'amount', 'user']


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Category, CategoryAdmin)
