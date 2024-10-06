from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from E_Auction.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('auctions', auctions, name="auctions"),
    path('product/<int:a_id>', product, name="product"),
    path('login', handlelogin, name="handlelogin"),
    path('logout', logout, name="logout"),
    path('register', register, name="register"),
    path('auc_participate/<int:a_id>', auc_participate, name="auc_participate"), # type: ignore
    path('auc_bid/<int:a_id>', auc_bid, name="auc_bid"),
    path('auc_add', auc_add, name="auc_add"),
    path('auc_del/<int:a_id>', auc_del, name="auc_del"), # type: ignore
    # path('auc_edit/<int:a_id>', auc_edit, name="auc_edit"), # type: ignore
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
