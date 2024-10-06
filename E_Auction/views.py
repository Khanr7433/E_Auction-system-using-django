from django.shortcuts import render, redirect, get_object_or_404
# Below module have Login, Logout & authenticate methods.
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from .models import *
from django.contrib.auth.decorators import login_required
today = date.today()


def home(request):
    auctions = Auction.objects.all().values()
    params = {"Auction": auctions}
    return render(request, 'home.html', params)


def auctions(request):
    auctions = Auction.objects.all().values()
    params = {"Auction": auctions}
    return render(request, 'auctions.html', params)


def contact(request):
    return render(request, 'contact.html')


def product(request, a_id):
    user = User.objects.get(username=request.user.username)
    product = Auction.objects.get(a_id=a_id)
    rel = Auction.objects.all().values()
    bid = Bid.objects.filter(a_id=a_id).values().order_by('-bid_amt')

    end_time = product.auct_start + product.duration
    rem_time = end_time - timezone.now()
    rem_sec = rem_time.total_seconds()

    prod = {"product": product}
    relprod = {"relprod": rel}
    bids = {"bids": bid}

    if rem_time.total_seconds() < 0:
        rem_time = 0  # Auction has already ended

        highest_bid = Bid.objects.filter(a_id=a_id).first()

        if not Result.objects.filter(auction=a_id).exists():
            if highest_bid:
                Result.objects.create(
                    user=user, auction=product, high_bid=highest_bid.bid_amt)

        params = {
            "prod": prod,
            "relprod": relprod,
            "highest_bid": highest_bid,
            "rem_time": rem_sec
        }
        return render(request, 'product.html', params)

    params = {
        "prod": prod,
        "relprod": relprod,
        "bids": bids,
        "rem_time": rem_sec
    }
    return render(request, 'product.html', params)


def about(request):
    return render(request, 'about.html')


def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully Logged In.')
            return redirect('home')
        else:
            messages.error(request, 'Invlid Credentials, Please try again.')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully Logged Out.')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.all().values()
        for i in user:
            flag = 0
            dataemail = i['email']
            if dataemail == email:
                flag = 1
                messages.error(request, 'Email ID Already Exist.')
            if flag != 1:
                new = User.objects.create_user(
                    email=email, username=username, password=password)
                new.name = name  # type: ignore
                new.phone = phone  # type: ignore
                new.save()
                messages.success(
                    request, 'Congratulation! Reigtered Successfully')
                return redirect('handlelogin')
    return render(request, 'register.html')


def auc_participate(request, a_id):
    user = User.objects.get(username=request.user.username)
    id = Auction.objects.get(a_id=a_id)
    part = Participant.objects.all().filter(
        User_name=user).filter(a_id=a_id).exists()
    if part:
        messages.error(
            request, 'You have already participated in this Auction')
        return redirect('product', a_id)
    else:
        if request.method == 'POST':
            new = Participant.objects.create(
                User_name=user, a_id=id)
            new.save()
            messages.success(
                request, "You have Successfully participated in this Auction")
            return redirect('product', a_id)


def auc_bid(request, a_id):
    auction = get_object_or_404(Auction, a_id=a_id)
    user = User.objects.get(username=request.user.username)
    id = Auction.objects.get(a_id=a_id)

    # Check if the user is a participant
    if not Participant.objects.filter(User_name=request.user, a_id=a_id).exists():
        messages.error(
            request, "You must Prticipate in the auction before placing a bid.")
        return redirect('product', a_id)
    else:
        if request.method == 'POST':
            bid = request.POST['bid_amt']
            last_bid = Bid.objects.filter(
                a_id=a_id).order_by('-bid_time').first()
            last_bid = last_bid.bid_amt if last_bid else 0

            if int(bid) > last_bid:
                new_bid = Bid(
                    a_id=id, user=user, bid_amt=bid)
                new_bid.save()
                messages.success(request, "Bid placed successfully!")
            else:
                messages.error(
                    request, "Your bid is lower than the current bid!")
    return redirect('product', a_id)


def auc_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        Description = request.POST['Description']
        Category = request.POST['Category']
        EntryFee = request.POST['EntryFee']
        OpenningBid = request.POST['OpenningBid']
        AuctionStart = request.POST['AuctionStart']
        Image = request.FILES['Image']

        auction = Auction.objects.create(
            title=title,
            desc=Description,
            category=Category,
            entry_fee=EntryFee,
            open_bid=OpenningBid,
            auct_start=AuctionStart,
            image=Image
        )
        auction.save()
        messages.success(
            request, 'Auction Added Succesfully')
        return redirect('auctions')

    return render(request, "auc_add.html")


def auc_del(request, a_id):
    auctions = Auction.objects.all().values()
    params = {"Auction": auctions}

    if request.method == 'POST':
        if Auction.objects.filter(a_id=a_id).delete():
            messages.success(request, "Auction Deleted Succesfully")
        else:
            messages.error(request, " Error")
        return redirect('auctions')

    return render(request, "auctions.html", params)


# def auc_edit(request, a_id):
#     if request.method == 'POST':
#         # title = request.POST['title']
#         # Description = request.POST['Description']
#         # Category = request.POST['Category']
#         # EntryFee = request.POST['EntryFee']
#         # OpenningBid = request.POST['OpenningBid']
#         # AuctionStart = request.POST['AuctionStart']
#         # Image = request.FILES['Image']
        
#         title = request.POST.get('title', '')
#         Description = request.POST.get('Description', '')
#         Category = request.POST.get('Category', '')
#         EntryFee = request.POST.get('EntryFee', 0)
#         OpenningBid = request.POST.get('OpenningBid', 0)
#         AuctionStart = request.POST.get('AuctionStart', '0')
#         Image = request.FILES.get('Image', '')

#         Auction.objects.filter(a_id=a_id).update(
#             title=title,
#             desc=Description,
#             category=Category,
#             entry_fee=EntryFee,
#             open_bid=OpenningBid,
#             auct_start=parse_datetime(AuctionStart),
#             image=Image
#         )
#         messages.success(
#             request, 'Auction Edited Succesfully')
#         return redirect('auctions')
    
#     auction = get_object_or_404(Auction, a_id=a_id)
#     return render(request, "auc_edit.html", {'auction': auction})

