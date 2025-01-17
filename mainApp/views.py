from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
def home_page(request):
    supercategories=Supercategory.objects.all()[:7]
    maincategories=Maincategory.objects.all()
    categories=Category.objects.all()
    subcategories=Subcategory.objects.all()
    products=Product.objects.all().order_by('id').reverse()[:6]
    try:
       brands_we_love=Product.objects.filter(offers=Supercategory.objects.get(slug="brands-we-love"))
    except:
       pass
    context = {
        'supercategories': supercategories,'maincategories': maincategories, 'categories': categories, 'subcategories': subcategories,
        'products': products,'brands_we_love':brands_we_love
    }
    return render(request,'front/index.html',context)


def product_by_maincategory_category(request,mcat,cat):
    try:
        data=Product.objects.filter(maincategory=Maincategory.objects.get(slug=mcat),category=Category.objects.get(slug=cat))
    except:
        data=''
    return render(request,'front/products.html',{'data':data})

def offers_page(request, cat):
    maincategories = Maincategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()

    # Filtering logic
    data = Product.objects.filter(offers=Supercategory.objects.get(slug=cat))

    # Apply filters based on selected checkboxes
    selected_maincategories = request.GET.getlist('maincategory[]')
    selected_categories = request.GET.getlist('category[]')
    selected_subcategories = request.GET.getlist('subcategory[]')
    selected_brands = request.GET.getlist('brand[]')
    selected_colors = request.GET.getlist('color[]')
    selected_size = request.GET.get('size')

    # Validate and filter only numeric values
    selected_maincategories = [mc for mc in selected_maincategories if mc.isdigit()]
    selected_categories = [cat for cat in selected_categories if cat.isdigit()]
    selected_subcategories = [sub for sub in selected_subcategories if sub.isdigit()]
    selected_brands = [brand for brand in selected_brands if brand.isdigit()]
    

    if selected_maincategories:
        data = data.filter(maincategory__id__in=selected_maincategories)
    if selected_categories:
        data = data.filter(category__id__in=selected_categories)
    if selected_subcategories:
        data = data.filter(subcategory__id__in=selected_subcategories)
    if selected_brands:
        data = data.filter(brand__id__in=selected_brands)
    if selected_colors:
        data = data.filter(color__in=selected_colors)
    if selected_size:
        data = data.filter(size=selected_size)

    # Pagination
    paginator = Paginator(data, 100)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))

    return render(request, 'front/products.html', {
        'page_posts': page_posts,
        'page_range': page_range,
        'maincategories': maincategories,
        'categories': categories,
        'subcategories': subcategories,
        'brands': brands,
        'size': size,
        'color': color,
        'selected_maincategories': selected_maincategories, 
        'selected_categories': selected_categories,
        'selected_subcategories': selected_subcategories,
        'selected_brands': selected_brands, 
        'selected_colors':selected_colors,
        'selected_size':selected_size,
    })



def category_page(request,cat):
    maincategories=Maincategory.objects.all()
    categories=Category.objects.all()
    subcategories=Subcategory.objects.all()
    brands=Brand.objects.all()
    size=Size.objects.all()
    color=Color.objects.all()
    try:
        # Fetch products with offers
        if cat == "all":
            data = Product.objects.all().order_by('-id')  # Filter products with non-empty offers
        else:
            # Get the Supercategory object
            data = Product.objects.filter(category=Category.objects.get(slug=cat))
        paginator = Paginator(data, 100)  # Show 10 posts per page
        page_number = request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        current_page = page_posts.number
        total_pages = paginator.num_pages
        page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    except Exception as e:
        print(f"Error occurred: {e}")  # Log the error for debugging
        data = Product.objects.none()  # Return an empty queryset
        
    return render(request, 'front/products.html', {'page_posts':page_posts,'page_range': page_range,'maincategories':maincategories,'categories':categories,'subcategories':subcategories,'brands':brands,'size':size,'color':color})


def men_home_page(request):
    return render(request,'front/home-men.html')

def kid_home_page(request):
    return render(request,'front/home-kids.html')

def brand_page(request):
    return render(request,'front/brands.html')

def product_page(request,cat):
    try:
       data=Product.objects.filter(cateory=Category.objects.get(slug=cat))
    except:
        data=''
    return render(request,'front/products.html',{'data':data})


def product_detail(request,name,id):
    try:
        data=get_object_or_404(Product,id=id)
        skuProduct=Product.objects.filter(sku=data.sku).exclude(id=data.id)
        similarProduct=Product.objects.filter(category=data.category).exclude(id=data.id)
    except:
        return HttpResponse("Technical issue...")
    return render(request,'front/product-detail.html',{'data':data,'skuProduct':skuProduct,'similarProduct':similarProduct})


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

