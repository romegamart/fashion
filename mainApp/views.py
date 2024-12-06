from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'front/index.html')

def men_home_page(request):
    return render(request,'front/home-men.html')

def kid_home_page(request):
    return render(request,'front/home-kids.html')

def brand_page(request):
    return render(request,'front/brands.html')

def product_page(request):
    return render(request,'front/products.html')

def product_detail(request):
    return render(request,'front/product-detail.html')

def cart_page(request):
    return render(request,'front/cart.html')

def wishlist_page(request):
    return render(request,'front/wishlist.html')

def compare_page(request):
    return render(request,'front/compare.html')

def checkout_page(request):
    return render(request,'front/checkout.html')

def blog_page(request):
    return render(request,'front/blog-grid.html')

def blog_details_page(request):
    return render(request,'front/blog-detail.html')

def about_us(request):
    return render(request,'front/about-us.html')

def contact_page(request):
    return render(request,'front/contact.html')

def faq(request):
    return render(request,'front/faq.html')


#User dashboard
def register(request):
    return render(request,'front/register.html')

def login(request):
    return render(request,'front/login.html')

def my_account(request):
    return render(request,'front/my-account.html')

def my_account_address(request):
    return render(request,'front/my-account-address.html')

def my_account_edit(request):
    return render(request,'front/my-account-edit.html')

def my_account_order(request):
    return render(request,'front/my-account-orders.html')

def my_account_order_details(request):
    return render(request,'front/my-account-orders-details.html')

def order_tracking(request):
    return render(request,'front/order-tracking.html')

def payment_confirmation(request):
    return render(request,'front/payment-confirmation.html')

def payment_failure(request):
    return render(request,'front/payment-failure.html')
