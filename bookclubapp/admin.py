from django.contrib import admin
from .models import User, Address, CreditCard, Book, BookList, Genre, GenreList, Delivery, AuctionItem, Bid, Record, AuctionStatistics, Register

# Register your models here.

admin.site.register(User)
admin.site.register(Address)
admin.site.register(CreditCard)
admin.site.register(Book)
admin.site.register(BookList)
admin.site.register(Genre)
admin.site.register(GenreList)
admin.site.register(Delivery)
admin.site.register(AuctionItem)
admin.site.register(Bid)
admin.site.register(Record)
admin.site.register(AuctionStatistics)
admin.site.register(Register)