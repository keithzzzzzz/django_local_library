from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username_user = models.CharField(max_length=20, primary_key=True, default=" ") #pk
    fname_user = models.CharField(max_length=20, default=" ")
    mname_user = models.CharField(max_length=20, default=" ")
    lname_user = models.CharField(max_length=20, default=" ")
    usertype_user = models.CharField(max_length=20, default=" ")
    password_user = models.CharField(max_length=20, default=" ")
    email_user = models.EmailField(max_length=254, default=" ")
    phone_user = models.CharField(max_length=15, default=" ")
    dob_user = models.DateField()
    gender_user = models.CharField(max_length=10, default=" ")
    kpoints_user = models.IntegerField()
    addr_id_user = models.IntegerField() #models.ForeignKey('Address',on_delete = models.CASCADE)
    cc_id_user = models.IntegerField() #models.ForeignKey('CreditCard', on_delete = models.CASCADE)

    def __str__(self):
        return self.username

class Address(models.Model):
    addr_id_addr = models.AutoField(primary_key=True) #pk
    addr_line_1_addr = models.CharField(max_length=254, default=" ")
    addr_line_2_addr = models.CharField(max_length=254,blank=True, default=" ")
    city_addr = models.CharField(max_length=254, default=" ")
    state_addr = models.CharField(max_length=254, default=" ")
    zip_code_addr = models.CharField(max_length=10, default=" ")

    def __str__(self):
        return 'Address 1:  %s' % (self.addr_line_1)

class CreditCard(models.Model):
    cc_id_cc = models.IntegerField(primary_key=True) #pk
    card_name_cc = models.CharField(max_length=40, default=" ")
    exp_date_cc = models.DateField()
    sec_code_cc = models.IntegerField()

    def __str__(self):
        return self.card_name

class Book(models.Model):
    ISBN_book = models.CharField(max_length=20,primary_key=True, default=" ") #pk
    rating_book = models.IntegerField()
    pub_date_book = models.DateField()
    pages_book = models.IntegerField()
    summary_book = models.TextField(default=" ")
    age_group_book = models.CharField(max_length=20, default=" ") # Maybe change/remove
    publisher_book = models.CharField(max_length=20, default=" ")
    author_book = models.CharField(max_length=20, default=" ")
    title_book = models.CharField(max_length=40, default=" ")

    def __str__(self):
        return self.title

class Genre(models.Model):
    ISBN_genre = models.IntegerField()#models.ForeignKey('Book',on_delete=models.CASCADE) #pk
    genre_id_genre = models.IntegerField()#models.ForeignKey('GenreList',on_delete=models.CASCADE) #pk

class GenreList(models.Model):
    genre_id_GL = models.AutoField(primary_key=True) #pk
    genre_name_GL = models.CharField(max_length=254, default=" ")

    def __str__(self):
        return genre_name

class BookList(models.Model):
    class Meta:
        unique_together=(('username_BL','ISBN_BL'),)
    username_BL = models.CharField(max_length=20, default=" ") #pk
    ISBN_BL = models.CharField(max_length=20,primary_key=True, default=" ")
    comments_BL = models.CharField(max_length=254, default=" ")

class Telemarketing(models.Model):
    class Meta:
        unique_together=(('username_tel','week_tel'),)
    username_tel = models.CharField(max_length=20, primary_key=True, default=" ") #CompPK
    week_tel = models.CharField(max_length=10, default=" ") # CompPK
    addr_id_tel = models.IntegerField()
    email_tel = models.CharField(max_length = 20, default=" ")
    gender_tel = models.CharField(max_length = 20, default=" ")
    phone_tel = models.CharField(max_length=15, default=" ")
    age_tel = models.IntegerField()

class Delivery(models.Model):
    shipping_no_del = models.AutoField(primary_key=True) #pk
    username_del = models.CharField(max_length=20, default=" ")
    item_id_del = models.IntegerField()
    start_date_del = models.DateField()
    end_date_del = models.DateField()

    def __str__(self):
        return 'Shipping Number %d' % (self.shipping_no)

class AuctionItem(models.Model):
    item_id_AI = models.AutoField(primary_key = True, default=" ") #pk
    buyout_price_AI = models.FloatField()    
    pub_id_AI = models.CharField(max_length=20, default=" ")
    desc_AI = models.CharField(max_length=254, default=" ")
    quantity_AI = models.IntegerField()

    def __str__(self):
        return 'Item ID: %d' % (self.item_id)

class Bid(models.Model):
    bid_id_bid = models.AutoField(primary_key = True) #pk
    starting_bid = models.IntegerField()
    bid_amount_bid = models.IntegerField()
    username_bid = models.CharField(max_length=20, default=" ")#models.ForeignKey('User', on_delete=models.CASCADE)
    item_id_bid = models.IntegerField()#models.ForeignKey('AuctionItem', on_delete=models.CASCADE)
    current_bid_bid = models.IntegerField()

    def __str__(self):
        return ' Bid ID: %d' % (self.bid_id)

class Register(models.Model):
    register_id_reg = models.AutoField(primary_key = True) #pk
    username_reg = models.CharField(max_length=20, default=" ")#models.ForeignKey('User', on_delete=models.CASCADE)
    item_id_reg = models.IntegerField()#models.ForeignKey('AuctionItem', on_delete=models.CASCADE)
    start_date_reg = models.DateField()
    end_date_reg = models.DateField()

class Record(models.Model):
    class Meta:
        unique_together=(('week_id_rec','item_id_rec'),)
    item_id_rec = models.IntegerField(primary_key=True) #pk
    stat_id_rec = models.IntegerField() #pk
    week_id_rec = models.IntegerField() #pk

    def __str__(self):
        return self.stat_id

class AuctionStatistics(models.Model):
    class Meta:
        unique_together=(('week_id_AS','stat_id_AS'),)
    week_id_AS = models.IntegerField() #pk
    stat_id_AS = models.IntegerField(primary_key=True) #pk
    num_bids_AS = models.IntegerField()
    total_sales_AS = models.FloatField()
    highest_bid_AS = models.IntegerField()

    def __str__(self):
        return self.week_id
