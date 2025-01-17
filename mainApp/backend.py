from django.shortcuts import render
import requests
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404



#API
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from io import StringIO
import json
import io
from .serializers import *


def is_superuser(user):
    return user.is_superuser


# Function to store the image on the external server
def image_store(image_type, image_file):
    print("Function is called...")
    base_url = "https://naricreationimage.pythonanywhere.com/add-image/"
    files = {
        'image': image_file  # Directly send the file object
    }
    data = {
        'image_type': image_type
    }

    try:
        response = requests.post(base_url, data=data, files=files)
        if response.status_code == 201:
            response_data = response.json()
            image_url = response_data.get("image_url")
            print(f"Image URL retrieved: {image_url}")
            return image_url  # Extract and return the image URL
        else:
            print(f"Failed to upload image: {response.text}")
            return None
    except Exception as e:
        print(f"Error occurred during image upload: {e}")
        return None

# Function to save product with an uploaded image
def product_store(request):
    if request.method == "POST":
        # Get image type and uploaded image from the POST request
        image_type = request.POST.get('image_type')
        uploaded_image = request.FILES.get('image')

        if uploaded_image:
            # Call the image_store function to upload the image and get the URL
            image_url = image_store(image_type, uploaded_image)
        else:
            image_url = None

        # Proceed only if the image URL was successfully retrieved
        if image_url:
            product = Maincategory()
            product.name = request.POST.get('name')  # Get the product name
            product.image = image_url  # Assign the image URL to the product
            product.save()  # Save the product in the database
            return render(request, 'front/data.html', {"success": True, "image_url": image_url})
        else:
            return render(request, 'front/data.html', {"error": "Failed to upload image or save data."})

    return render(request, 'front/data.html')



def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("/admin-dashboard")
            else:
                messages.error(request, "You do not have admin privileges.")
        else:
            messages.error(request, "Invalid Username or Password!")
    
    return render(request, "backend/login.html")


@login_required(login_url='/admin-login')
def admin_dashboard(Request):
  if not Request.user.is_superuser:
      return HttpResponseForbidden("You don't have permission to access this page.")
  else:
    data=Product.objects.all().order_by('id').reverse()
    offers=Supercategory.objects.all().order_by('id').reverse()
    # prod=len(Product.objects.all())
    # ord=len(Order.objects.all())
    # sel=len(Seller.objects.all())
    # pen=len(Product.objects.filter(verification="Pending"))
    # act=len(Product.objects.filter(verification="Done"))
    # oos = len(Product.objects.filter(qty__lt=1))
    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = Request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    # return render(Request,'superadmin/index.html',{'page_posts':page_posts,'page_range': page_range,'prod':prod,'ord':ord,'sel':sel,'pen':pen,'act':act,'oos':oos})
    return render(Request,'backend/index.html',{'page_posts':page_posts,'page_range': page_range,'offers':offers})



#Maincategory
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_supercategory(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       
        supercategories=Supercategory.objects.all().order_by('id').reverse()
        if(Request.method=="POST"):
            m=Supercategory()
            m.name=Request.POST.get('name')
            m.slug=slugify(m.name)
            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            m.image=image_url
            
            m.save()
            return redirect('/supercategory')
        return render(Request,'backend/add-supercategory.html',{'supercategories':supercategories})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def supercategory_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        
        supercategory=Supercategory.objects.all().order_by('id').reverse()
        return render(Request,'backend/supercategory.html',{'supercategory':supercategory})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_supercategory(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        supercategories=Supercategory.objects.all().order_by('id').reverse()
        data=Supercategory.objects.get(id=id)
        if(Request.method=="POST"):
            data.name=Request.POST.get('name')
            data.slug=slugify(data.name)
            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            if(image_url):
                data.image=image_url
            
            data.save()
            return redirect('/supercategory')
        return render(Request,'backend/update-supercategory.html',{'data':data,'supercategories':supercategories})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_supercategory(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       data=Supercategory.objects.get(id=id)
       data.delete()
       return redirect('/supercategory')



#Maincategory
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_maincategory(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       
        maincategories=Maincategory.objects.all().order_by('id').reverse()
        if(Request.method=="POST"):
            m=Maincategory()
            m.name=Request.POST.get('name')
            m.slug=slugify(m.name)
            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            m.image=image_url
            m.title=Request.POST.get('title')
            m.description=Request.POST.get('description')
            m.save()
            return redirect('/maincategory')
        return render(Request,'backend/add-maincategory.html',{'maincategories':maincategories})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def maincategory_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        
        maincategory=Maincategory.objects.all().order_by('id').reverse()
        return render(Request,'backend/maincategory.html',{'maincategory':maincategory})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_maincategory(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        maincategories=Maincategory.objects.all().order_by('id').reverse()
        data=Maincategory.objects.get(id=id)
        if(Request.method=="POST"):
            data.name=Request.POST.get('name')
            data.slug=slugify(data.name)
            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            if(image_url):
                data.image=image_url
            
            data.title=Request.POST.get('title')
            data.description=Request.POST.get('description')
            data.save()
            return redirect('/maincategory')
        return render(Request,'backend/update-maincategory.html',{'data':data,'maincategories':maincategories})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_maincategory(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       data=Maincategory.objects.get(id=id)
       data.delete()
       return redirect('/maincategory')


#category
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_category(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        
        mcat=Maincategory.objects.all().order_by('id').reverse()
        if(Request.method=="POST"):
            c=Category()
            c.maincategory=Maincategory.objects.get(name=Request.POST.get('maincategory'))
            c.name=Request.POST.get('name')
            c.slug=slugify(c.name)
            spec_keys = Request.POST.getlist('spec_key[]')
            spec_values = Request.POST.getlist('spec_value[]')

            if len(spec_keys) == len(spec_values):
                specifications = {key: value for key, value in zip(spec_keys, spec_values)}
                c.specifications = specifications

            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            if(image_url):
                c.image=image_url
            
            c.title=Request.POST.get('title')
            c.description=Request.POST.get('description')

            if Category.objects.filter(maincategory=c.maincategory ,name=c.name):
                messages.error(Request, "A category with this name already exists under the selected maincategory.")
                return render(Request, 'backend/update-subcategory.html', {
                    'mcat':mcat
                })
            c.save()
            return redirect('/category')
        return render(Request,'backend/add-category.html',{'mcat':mcat})


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def category_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        
        category=Category.objects.all().order_by('id').reverse()
        return render(Request,'backend/category.html',{'category':category})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_category(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")

    # Fetch the category and main categories
    data = get_object_or_404(Category, id=id)
    mcat = Maincategory.objects.all()

    if request.method == "POST":
        data.maincategory = Maincategory.objects.get(id=request.POST.get('maincategory'))
        data.name = request.POST.get('name')
        data.slug = slugify(data.name)

        # Handle specifications
        spec_keys = request.POST.getlist('spec_key[]')
        spec_values = request.POST.getlist('spec_value[]')
        if len(spec_keys) == len(spec_values):
            data.specifications = {key: value for key, value in zip(spec_keys, spec_values)}

        # Handle image upload
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            image_url = image_store("category", uploaded_image)  # Replace with your actual image upload logic
            data.image = image_url

        # Meta fields
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')

        # Save updated category
        data.save()
        return redirect('/category')

    return render(request, 'backend/update-category.html', {'data': data, 'mcat': mcat})


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_category(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        data=Category.objects.get(id=id)
        data.delete()
    return redirect('/category')



#subcategory
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_subcategory(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        
        subcategories=Subcategory.objects.all().order_by('id').reverse()
        scat=Category.objects.all().order_by('id').reverse()
        if(Request.method=="POST"):
            c=Subcategory()
            c.category=Category.objects.get(name=Request.POST.get('category'))
            c.name=Request.POST.get('name')
            c.slug=slugify(c.name)
            

            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            if(image_url):
                c.image=image_url
            
            c.title=Request.POST.get('title')
            c.description=Request.POST.get('description')
            if Subcategory.objects.filter(category=c.category ,name=c.name):
                print("Already Exist...")
                messages.error(Request, "A subcategory with this name already exists under the selected category.")
                return render(Request, 'backend/add-subcategory.html', {
                    'scat':scat
                })
            c.save()
            return redirect('/subcategory')
        return render(Request,'backend/add-subcategory.html',{'scat':scat,'subcategories':subcategories})


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def subcategory_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        
        subcategory=Subcategory.objects.all().order_by('id').reverse()
        return render(Request,'backend/subcategory.html',{'subcategory':subcategory})
    

    
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_subcategory(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")

    # Fetch subcategory and categories
    subcategories = Subcategory.objects.all()
    data = get_object_or_404(Subcategory, id=id)
    scat = Category.objects.all()

    if request.method == "POST":
        category = Category.objects.get(id=request.POST.get('category'))
        name = request.POST.get('name')
        slug = slugify(name)

        # Check for duplicate name within the selected category
        if Subcategory.objects.filter(category=category, name=name).exclude(id=data.id).exists():
            messages.error(request, "A subcategory with this name already exists under the selected category.")
            return render(request, 'backend/update-subcategory.html', {
                'data': data, 'scat': scat, 'subcategories': subcategories
            })

        # Handle slug uniqueness
        original_slug = slug
        counter = 1
        while Subcategory.objects.filter(slug=slug).exclude(id=data.id).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1

        # Update data
        data.category = category
        data.name = name
        data.slug = slug

        # Handle image upload
        uploaded_image = request.FILES.get('image')
        if uploaded_image:
            image_url = image_store("category", uploaded_image)  # Replace with your actual upload logic
            data.image = image_url

        # Update meta fields
        data.title = request.POST.get('title', '').strip()
        data.description = request.POST.get('description', '').strip()

        # Save the updated subcategory
        data.save()
        messages.success(request, "Subcategory updated successfully.")
        return redirect('/subcategory')

    return render(request, 'backend/update-subcategory.html', {
        'data': data, 'scat': scat, 'subcategories': subcategories
    })

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_subcategory(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        data=Subcategory.objects.get(id=id)
        data.delete()
    return redirect('/subcategory')



#Brand
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_brand(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       
        brand=Brand.objects.all()
        if(Request.method=="POST"):
            m=Brand()
            m.name=Request.POST.get('name')
            m.slug=slugify(m.name)
            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            m.image=image_url
            m.title=Request.POST.get('title')
            m.description=Request.POST.get('description')
            if Brand.objects.filter(name=m.name):
                print("Already Exist...")
                messages.error(Request, "A brand with this name already exists.")
                return render(Request, 'backend/add-brand.html', {
                    'brand':brand
                })
            m.save()
            return redirect('/brand')
        return render(Request,'backend/add-brand.html',{'brand':brand})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def brand_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        
        brand=Brand.objects.all().order_by('id').reverse()
        return render(Request,'backend/brand.html',{'brand':brand})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_brand(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        
        data=Brand.objects.get(id=id)
        if(Request.method=="POST"):
            data.name=Request.POST.get('name')
            data.slug=slugify(data.name)
            uploaded_image=Request.FILES.get('image')
            if uploaded_image:
            # Call the image_store function to upload the image and get the URL
               image_url = image_store("category", uploaded_image)
            else:
                image_url = None
            if(image_url):
                data.image=image_url
            
            data.title=Request.POST.get('title')
            data.description=Request.POST.get('description')
            if Brand.objects.filter(name=data.name).exclude(id=data.id).exists():
                print("Already Exist...")
                messages.error(Request, "A brand with this name already exists.")
                return render(Request, 'backend/update-brand.html', {
                    'data':data
                })
            data.save()
            return redirect('/brand')
        return render(Request,'backend/update-brand.html',{'data':data})


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_brand(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       data=Brand.objects.get(id=id)
       data.delete()
       return redirect('/brand')



#color
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_color(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       
        color=Color.objects.all()
        if(Request.method=="POST"):
            m=Color()
            m.name=Request.POST.get('name')
            if Color.objects.filter(name=m.name):
                print("Already Exist...")
                messages.error(Request, "A color with this name already exists.")
                return render(Request, 'backend/add-color.html', {
                    'm':m
                })
            m.save()
            return redirect('/color')
        return render(Request,'backend/add-color.html',{'color':color})


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def color_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        color=Color.objects.all().order_by('id').reverse()
        return render(Request,'backend/color.html',{'color':color})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_color(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        
        data=Color.objects.get(id=id)
        if(Request.method=="POST"):
            data.name=Request.POST.get('name')
            if Color.objects.filter(name=data.name).exclude(id=data.id).exists():
                print("Already Exist...")
                messages.error(Request, "A color with this name already exists.")
                return render(Request, 'backend/update-color.html', {
                    'data':data
                })
            data.save()
            return redirect('/color')
        return render(Request,'backend/update-color.html',{'data':data})


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_color(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       data=Color.objects.get(id=id)
       data.delete()
       return redirect('/color')


#Size
@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_size(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       
        size=Size.objects.all()
        if(Request.method=="POST"):
            m=Size()
            m.name=Request.POST.get('name')
            if Size.objects.filter(name=m.name):
                print("Already Exist...")
                messages.error(Request, "A color with this name already exists.")
                return render(Request, 'backend/add-size.html', {
                    'm':m
                })
            m.save()
            return redirect('/size')
        return render(Request,'backend/add-size.html',{'size':size})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def size_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        size=Size.objects.all().order_by('id').reverse()
        return render(Request,'backend/size.html',{'size':size})

@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_size(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
        
        data=Size.objects.get(id=id)
        if(Request.method=="POST"):
            data.name=Request.POST.get('name')
            if Size.objects.filter(name=data.name).exclude(id=data.id):
                print("Already Exist...")
                messages.error(Request, "A color with this name already exists.")
                return render(Request, 'backend/update-size.html', {
                    'data':data
                })
            data.save()
            return redirect('/size')
        return render(Request,'backend/update-size.html',{'data':data})


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_size(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else:  
       data=Size.objects.get(id=id)
       data.delete()
       return redirect('/size')


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def add_product(request):
    mcat = Maincategory.objects.all().order_by('-id')
    cat = Category.objects.all().order_by('-id')
    scat = Subcategory.objects.all().order_by('-id')
    brnd = Brand.objects.all().order_by('-id')
    clr = Color.objects.all().order_by('-id')
    sz = Size.objects.all().order_by('-id')

    if request.method == "POST":
        product = Product()

        # Assign related fields
        product.maincategory = Maincategory.objects.get(name=request.POST.get('maincategory'))
        product.category = Category.objects.get(maincategory=product.maincategory,name=request.POST.get('category'))
        product.subcategory = Subcategory.objects.get(name=request.POST.get('subcategory'))
        product.brand = Brand.objects.get(name=request.POST.get('brand'))

        # Upload images
        for i in range(1, 5):
            uploaded_image = request.FILES.get(f'image{i}')
            if uploaded_image:
                image_url = image_store("product", uploaded_image)
                setattr(product, f'image{i}', image_url)

        # Assign other fields
        product.name = request.POST.get('name')
        try:
            # Get base price and discount from the POST request
            base_price = float(request.POST.get('price', 0))
            discount = float(request.POST.get('discount', 0))

            # Validate inputs
            if base_price < 0 or discount < 0:
                return JsonResponse({'error': 'Base price and discount must be non-negative'}, status=400)

            # Calculate the final price
            final_price = base_price - (base_price * discount / 100)

            # Assign values to the product model
            product.base_price = base_price
            product.discount = discount
            product.price = round(final_price, 2)  # Round the price to 2 decimal places

        except ValueError:
            # Handle invalid inputs (e.g., non-numeric values)
            return JsonResponse({'error': 'Invalid price or discount format'}, status=400)


        product.quantity = int(request.POST.get('quantity'))
        product.size = request.POST.get('size')
        product.color = request.POST.get('color')
        product.rating = float(request.POST.get('rating', 0))
        product.reviews = int(request.POST.get('reviews', 0))
        product.description = request.POST.get('description')
        product.sku = request.POST.get('sku', '')
        product.weight = request.POST.get('weight', '')
        product.length = request.POST.get('length', '')
        product.width = request.POST.get('width', '')
        product.height = request.POST.get('height', '')

        # Handle specifications
        spec_keys = request.POST.getlist('spec_key[]')
        spec_values = request.POST.getlist('spec_value[]')

        # Ensure lengths match and validate data
        if len(spec_keys) == len(spec_values):
            specifications = {}
            for key, value in zip(spec_keys, spec_values):
                if key.strip() and value.strip():  # Ensure neither key nor value is empty
                    specifications[key.strip()] = value.strip()
            product.specifications = specifications
        else:
            # Handle the error if lengths do not match
            return JsonResponse({'error': 'Mismatched specification keys and values'}, status=400)


        # Handle FAQs
        faq_keys = request.POST.getlist('faq_key[]')
        faq_values = request.POST.getlist('faq_value[]')

        # Ensure lengths match and validate data
        if len(faq_keys) == len(faq_values):
            faqs = {}
            for key, value in zip(faq_keys, faq_values):
                if key.strip() and value.strip():  # Ensure neither key nor value is empty
                    faqs[key.strip()] = value.strip()
            product.faq = faqs
        else:
            # Handle the error if lengths do not match
            return JsonResponse({'error': 'Mismatched FAQ keys and values'}, status=400)

        # Save product
        product.save()
        return redirect('/product')

    context = {
        'maincategories': mcat, 'categories': cat, 'subcategories': scat,
        'brands': brnd, 'clr': clr, 'sz': sz
    }
    return render(request, 'backend/add-product.html', context)


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def product_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        
        data=Product.objects.all().order_by('id').reverse()
        paginator = Paginator(data, 100)  # Show 10 posts per page
        page_number = Request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        current_page = page_posts.number
        total_pages = paginator.num_pages
        page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
        # return render(Request,'superadmin/index.html',{'page_posts':page_posts,'page_range': page_range,'prod':prod,'ord':ord,'sel':sel,'pen':pen,'act':act,'oos':oos})
        return render(Request,'backend/products.html',{'page_posts':page_posts,'page_range': page_range})




@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_product(request,id,pn):
    mcat = Maincategory.objects.all().order_by('-id')
    cat = Category.objects.all().order_by('-id')
    scat = Subcategory.objects.all().order_by('-id')
    brnd = Brand.objects.all().order_by('-id')
    clr = Color.objects.all().order_by('-id')
    sz = Size.objects.all().order_by('-id')

    product= get_object_or_404(Product,id=id)
    if request.method == "POST":

        # Assign related fields
        product.maincategory = Maincategory.objects.get(name=request.POST.get('maincategory'))
        product.category = Category.objects.get(maincategory=product.maincategory,name=request.POST.get('category'))
        product.subcategory = Subcategory.objects.get(name=request.POST.get('subcategory'))
        product.brand = Brand.objects.get(name=request.POST.get('brand'))

        # Upload images
        for i in range(1, 5):
            uploaded_image = request.FILES.get(f'image{i}')
            if uploaded_image:
                image_url = image_store("product", uploaded_image)
                setattr(product, f'image{i}', image_url)

        # Assign other fields
        product.name = request.POST.get('name')
        try:
            # Get base price and discount from the POST request
            base_price = float(request.POST.get('price', 0))
            discount = float(request.POST.get('discount', 0))

            # Validate inputs
            if base_price < 0 or discount < 0:
                return JsonResponse({'error': 'Base price and discount must be non-negative'}, status=400)

            # Calculate the final price
            final_price = base_price - (base_price * discount / 100)

            # Assign values to the product model
            product.base_price = base_price
            product.discount = discount
            product.price = round(final_price, 2)  # Round the price to 2 decimal places

        except ValueError:
            # Handle invalid inputs (e.g., non-numeric values)
            return JsonResponse({'error': 'Invalid price or discount format'}, status=400)


        product.quantity = int(request.POST.get('quantity'))
        product.size = request.POST.get('size')
        product.color = request.POST.get('color')
        product.rating = float(request.POST.get('rating', 0))
        product.reviews = int(request.POST.get('reviews', 0))
        product.description = request.POST.get('description')
        product.sku = request.POST.get('sku', '')
        product.weight = request.POST.get('weight', '')
        product.length = request.POST.get('length', '')
        product.width = request.POST.get('width', '')
        product.height = request.POST.get('height', '')

        # Handle specifications
        spec_keys = request.POST.getlist('spec_key[]')
        spec_values = request.POST.getlist('spec_value[]')

        # Ensure lengths match and validate data
        if len(spec_keys) == len(spec_values):
            specifications = {}
            for key, value in zip(spec_keys, spec_values):
                if key.strip() and value.strip():  # Ensure neither key nor value is empty
                    specifications[key.strip()] = value.strip()
            product.specifications = specifications
        else:
            # Handle the error if lengths do not match
            return JsonResponse({'error': 'Mismatched specification keys and values'}, status=400)


        # Handle FAQs
        faq_keys = request.POST.getlist('faq_key[]')
        faq_values = request.POST.getlist('faq_value[]')

        # Ensure lengths match and validate data
        if len(faq_keys) == len(faq_values):
            faqs = {}
            for key, value in zip(faq_keys, faq_values):
                if key.strip() and value.strip():  # Ensure neither key nor value is empty
                    faqs[key.strip()] = value.strip()
            product.faq = faqs
        else:
            # Handle the error if lengths do not match
            return JsonResponse({'error': 'Mismatched FAQ keys and values'}, status=400)

        # Save product
        product.save()
        return redirect('/product')

    context = {
        'maincategories': mcat, 'categories': cat, 'subcategories': scat,
        'brands': brnd, 'clr': clr, 'sz': sz,'data':product
    }
    return render(request, 'backend/update-product.html', context)



@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def product_page(Request):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        
        data=Product.objects.all().order_by('id').reverse()
        paginator = Paginator(data, 100)  # Show 10 posts per page
        page_number = Request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        current_page = page_posts.number
        total_pages = paginator.num_pages
        page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
        # return render(Request,'superadmin/index.html',{'page_posts':page_posts,'page_range': page_range,'prod':prod,'ord':ord,'sel':sel,'pen':pen,'act':act,'oos':oos})
        return render(Request,'backend/products.html',{'page_posts':page_posts,'page_range': page_range})




@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def duplicate_product(request,id,pn):
    mcat = Maincategory.objects.all().order_by('-id')
    cat = Category.objects.all().order_by('-id')
    scat = Subcategory.objects.all().order_by('-id')
    brnd = Brand.objects.all().order_by('-id')
    clr = Color.objects.all().order_by('-id')
    sz = Size.objects.all().order_by('-id')

    data= get_object_or_404(Product,id=id)
    product= Product()
    if request.method == "POST":

        # Assign related fields
        product.maincategory = Maincategory.objects.get(name=request.POST.get('maincategory'))
        product.category = Category.objects.get(maincategory=product.maincategory,name=request.POST.get('category'))
        product.subcategory = Subcategory.objects.get(name=request.POST.get('subcategory'))
        product.brand = Brand.objects.get(name=request.POST.get('brand'))

        # Upload images
        for i in range(1, 5):
            uploaded_image = request.FILES.get(f'image{i}')
            if uploaded_image:
                image_url = image_store("product", uploaded_image)
                setattr(product, f'image{i}', image_url)

        # Assign other fields
        product.name = request.POST.get('name')
        try:
            # Get base price and discount from the POST request
            base_price = float(request.POST.get('price', 0))
            discount = float(request.POST.get('discount', 0))

            # Validate inputs
            if base_price < 0 or discount < 0:
                return JsonResponse({'error': 'Base price and discount must be non-negative'}, status=400)

            # Calculate the final price
            final_price = base_price - (base_price * discount / 100)

            # Assign values to the product model
            product.base_price = base_price
            product.discount = discount
            product.price = round(final_price, 2)  # Round the price to 2 decimal places

        except ValueError:
            # Handle invalid inputs (e.g., non-numeric values)
            return JsonResponse({'error': 'Invalid price or discount format'}, status=400)


        product.quantity = int(request.POST.get('quantity'))
        product.size = request.POST.get('size')
        product.color = request.POST.get('color')
        product.rating = float(request.POST.get('rating', 0))
        product.reviews = int(request.POST.get('reviews', 0))
        product.description = request.POST.get('description')
        product.sku = request.POST.get('sku', '')
        product.weight = request.POST.get('weight', '')
        product.length = request.POST.get('length', '')
        product.width = request.POST.get('width', '')
        product.height = request.POST.get('height', '')

        # Handle specifications
        spec_keys = request.POST.getlist('spec_key[]')
        spec_values = request.POST.getlist('spec_value[]')

        # Ensure lengths match and validate data
        if len(spec_keys) == len(spec_values):
            specifications = {}
            for key, value in zip(spec_keys, spec_values):
                if key.strip() and value.strip():  # Ensure neither key nor value is empty
                    specifications[key.strip()] = value.strip()
            product.specifications = specifications
        else:
            # Handle the error if lengths do not match
            return JsonResponse({'error': 'Mismatched specification keys and values'}, status=400)


        # Handle FAQs
        faq_keys = request.POST.getlist('faq_key[]')
        faq_values = request.POST.getlist('faq_value[]')

        # Ensure lengths match and validate data
        if len(faq_keys) == len(faq_values):
            faqs = {}
            for key, value in zip(faq_keys, faq_values):
                if key.strip() and value.strip():  # Ensure neither key nor value is empty
                    faqs[key.strip()] = value.strip()
            product.faq = faqs
        else:
            # Handle the error if lengths do not match
            return JsonResponse({'error': 'Mismatched FAQ keys and values'}, status=400)

        # Save product
        product.save()
        return redirect('/product')

    context = {
        'maincategories': mcat, 'categories': cat, 'subcategories': scat,
        'brands': brnd, 'clr': clr, 'sz': sz,'data':data
    }
    return render(request, 'backend/update-product.html', context)


@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def delete_product(Request,id):
    if not Request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to access this page.")
    else: 
        data=get_object_or_404(Product,id=id)
        data.delete()
    return redirect('/product')



@login_required(login_url='/admin-login/')
@user_passes_test(is_superuser, login_url='/admin-login/')
def update_product_offers(request,id,ops):
    try:
       data=get_object_or_404(Product,id=id)
       ofr=get_object_or_404(Supercategory,slug=ops)
       if(data):
           data.offers=ofr
           data.save()
    except:
        return HttpResponse("Invalid action...")
    return redirect("/admin-dashboard")