
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('men/',views.men_home_page),
    path('kid/',views.kid_home_page),
    path('products/',views.product_page),
    path('product-detail/',views.product_detail),
    path('cart/',views.cart_page),
    path('wishlist/',views.wishlist_page),
    path('compare/',views.compare_page),
    path('checkout/',views.checkout_page),
    path('blog/',views.blog_page),
    path('blog-details/',views.blog_details_page),
    
    path('about-us/',views.about_us),
    path('brands/',views.brand_page),
    path('contact/',views.contact_page),
    path('faq/',views.faq),

    #User Dashboard
    path('login/',views.login),
    path('register/',views.register),
    path('my-account/',views.my_account),
    path('my-account-address/',views.my_account_address),
    path('my-account-edit/',views.my_account_edit),
    path('my-account-orders/',views.my_account_order),
    path('my-account-orders-details/',views.my_account_order_details),
    path('order-tracking/',views.order_tracking),
    path('payment-confirmation/',views.payment_confirmation),
    path('payment-failure/',views.payment_failure),
    
]
