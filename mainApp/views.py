from django.shortcuts import render
import requests
from django.http import HttpResponse,HttpResponseForbidden
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q



# Create your views here.
def home_page(request):
    supercategories=Supercategory.objects.all()[:7]
    maincategories=Maincategory.objects.all()
    categories=Category.objects.all()
    subcategories=Subcategory.objects.all()
    slider=Slider.objects.all()
    products=Product.objects.all().order_by('id').reverse()[:6]
    try:
       brands_we_love=Product.objects.filter(offers=Supercategory.objects.get(slug="brands-we-love"))
    except:
       pass
    context = {
        'supercategories': supercategories,'maincategories': maincategories, 'categories': categories, 'subcategories': subcategories,
        'products': products,'brands_we_love':brands_we_love,'slider':slider
    }
    return render(request,'front/index.html',context)

def category_by_maincategory(request,ops):
    return render(request,'front/categories.html')

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
    try:
        if cat == "all":
            data = Product.objects.filter(offers__isnull=False)
        else:
            supercategory = Supercategory.objects.get(slug=cat)
            data = Product.objects.filter(offers=supercategory)
    except Supercategory.DoesNotExist:
        data = Product.objects.none()  # Return an empty queryset


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

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Redirect based on user type or 'next' parameter
            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)
            elif user.is_superuser:
                return redirect("/admin-dashboard")  # Use reverse for named URL
            else:
                return redirect("/my-account") # Use reverse for named URL
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "front/login.html")



def logout_page(request):
    logout(request)
    return redirect("/login")

def register(request):
    if request.method == "POST":
        # Get the form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the user already exists
        if User.objects.filter(username=phone).exists():
            messages.error(request, "Phone number already exists.")
            return render(request, 'front/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'front/register.html')
        
        # Hash the password
        hashed_password = make_password(password)
        
        # Create a new buyer object
        buyer = Buyer(name=name, phone=phone, email=email, password=hashed_password)
        buyer.save()

        # Split the name into first and last names
        first_name, last_name = name.split(" ", 1) if " " in name else (name, "")
        
        # Create a new user object
        user = User(username=phone, email=email, first_name=first_name, last_name=last_name, password=hashed_password)
        user.save()

        # Authenticate and log the user in
        user = authenticate(username=phone, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("/admin-dashboard")
            else:
               return redirect('/my-account')
        else:
            messages.error(request, "Invalid Username or Password!")

          # Redirect to a page after successful login (e.g., home page)
    
    return render(request, 'front/register.html')



@login_required(login_url="/login")
def my_account(request):
    print("User: ",request.user.username)
    if not Buyer.objects.filter(phone=request.user.username):
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    buyer=Buyer.objects.get(phone=request.user.username)
    return render(request,'front/my-account.html',{'buyer':buyer})


def my_account_address(request):
    return render(request,'front/my-account-address.html')

def my_account_edit(request):
    return render(request,'front/my-account-edit.html')

@login_required(login_url="/login")
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


def search_product(request):
    maincategories = Maincategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()

    query = request.GET.get('query', '').strip()  # Get the query from GET request

    # Filter products based on the search query
    if query:
        data = Product.objects.filter(
            Q(name__icontains=query) |  # Search by name
            Q(description__icontains=query) |  # Search by description
            Q(category__name__icontains=query) |  # Search by category name
            Q(subcategory__name__icontains=query)  # Search by subcategory name
        ).distinct()  # Avoid duplicate results if multiple fields match
    else:
        data = Product.objects.none()  # If no query, return empty results

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
        'query': query,  # Pass the query to the template
    })
