from django.contrib import admin
from E_Auction.models import *
 
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Participant)
admin.site.register(Result)