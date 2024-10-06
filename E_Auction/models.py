from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User


class Auction(models.Model):
    a_id = models.AutoField(("Auction id"), primary_key=True)
    title = models.CharField(("Title"), max_length=50)
    desc = models.TextField(("Description"))
    category = models.CharField(("Category"), max_length=50)
    entry_fee = models.IntegerField(("Entry Fee"))
    open_bid = models.IntegerField(("Openning Bid"))
    auct_start = models.DateTimeField(
        ("Auction Start Date & Time"), auto_now=False, auto_now_add=False)
    duration = models.DurationField(
        ("Auction Duration"), default=timedelta(minutes=30))
    image = models.ImageField(
        ("image"), upload_to='Images/',  max_length=None)

    class Meta:
        verbose_name = "Auction"
        verbose_name_plural = "Auctions"
        db_table = "auctions"
        # order by auction start date in descending order
        ordering = ["-auct_start"]

    def __str__(self):
        return f"{self.title} , {self.open_bid}"


class Participant(models.Model):
    p_id = models.AutoField(("Participant Id"), primary_key=True)
    User_name = models.ForeignKey(User, verbose_name=(
        "Bidder Name"), on_delete=models.CASCADE)
    a_id = models.ForeignKey("E_Auction.Auction", verbose_name=(
        "Auction id"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Partcipants"
        db_table = "participants"
        # order by Participant Id in descending order
        ordering = ["-p_id"]

    def __str__(self):
        return f"{self.User_name} + {self.a_id}"


class Bid(models.Model):
    b_id = models.AutoField(("Bidder id"), primary_key=True)
    user = models.ForeignKey(User, verbose_name=(
        "Bidder Name"), on_delete=models.CASCADE)
    a_id = models.ForeignKey("E_Auction.Auction", verbose_name=(
        "Auction id"), on_delete=models.CASCADE)
    bid_amt = models.IntegerField(("Bid Amount"))
    bid_time = models.DateTimeField(("Bid Time"), auto_now_add=True)

    class Meta:
        verbose_name = "Bid"
        verbose_name_plural = "Bids"
        db_table = "bids"
        # order by bid amount in descending order
        ordering = ["-a_id", "-bid_amt"]

    def __str__(self):
        return f"{self.user} + {self.bid_amt} + {self.a_id}"


class Result(models.Model):
    r_id = models.AutoField(("Result ID"), primary_key=True)
    user = models.ForeignKey(User, verbose_name=(
        "Winner Name"), on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, verbose_name=(
        "Auction Name"), on_delete=models.CASCADE)
    high_bid = models.IntegerField(("Highest Bid"))
    end_datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        db_table = "Results"   

    def __str__(self):
        return f"Auction {self.auction.title} won by {self.user.username} with {self.high_bid}"


# class Payment(models.Model):
#     pass


# class Member_fee(models.Model):
#     pass


# class Status(models.Model):
#     pass


# class Send_Feedback(models.Model):
#     pass


# class Category(models.Model):
#     pass


# class Sub_Category(models.Model):
#     pass


# class Session_Time(models.Model):
#     pass


# class Session_date(models.Model):
#     pass


# class Product(models.Model):
#     pass


# class Participant(models.Model):
#     pass


# class Aucted_Product(models.Model):
#     pass
