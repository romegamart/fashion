#API
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import json
from django.db.models import Q



@csrf_exempt
def app_get_slider(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Slider.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = SliderSerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })




@csrf_exempt
def app_get_offers(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Supercategory.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = SupercategorySerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_maincategory(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Maincategory.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = MaincategorySerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_category(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Category.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = CategorySerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_subcategory(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Subcategory.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = SubcategorySerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_brand(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Brand.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = BrandSerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_size(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Size.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = SizeSerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_color(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Color.objects.all()
                if data:
                    # Serialize the data
                    dataSerializer = ColorSerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_product(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey != "!NARI!(^&*%@%!)":
            return JsonResponse({'status': False, 'message': "Invalid security key."})
        
        # Extract values for filtering
        selected_maincategories = request.POST.get('maincategory')
        selected_categories = request.POST.get('category')
        selected_subcategories = request.POST.get('subcategory')
        selected_offer = request.POST.get('offer')
        selected_colors = request.POST.get('color')
        selected_size = request.POST.get('size')

        print(f"""
              Maincategory: {selected_maincategories}
              Category: {selected_categories}
              Subcategory: {selected_subcategories}
              Offer: {selected_offer}
              Color: {selected_colors}
              Size: {selected_size}
              """)

        try:
            # Start filtering based on values (not IDs)
            data = Product.objects.all()

            if selected_maincategories:
                data = data.filter(maincategory__name=selected_maincategories)
            if selected_categories:
                data = data.filter(category__name=selected_categories)
            if selected_subcategories:
                data = data.filter(subcategory__name=selected_subcategories)
            if selected_offer:
                data = data.filter(offers__name=selected_offer)
            if selected_colors:
                data = data.filter(color=selected_colors)
            if selected_size:
                data = data.filter(size=selected_size)

            # Check if products match the criteria
            if data.exists():
                dataSerializer = ProductSerializer(data, many=True)
                return JsonResponse({
                    'status': True,
                    'message': "Data found successfully.",
                    'data': dataSerializer.data
                })
            else:
                return JsonResponse({
                    'status': False,
                    'message': "No products match the criteria."
                })
        except Exception as e:
            return JsonResponse({
                'status': False,
                'message': f"An error occurred: {str(e)}"
            })

    # Return error for non-POST requests
    return JsonResponse({'status': False, 'message': "Invalid request method."})




@csrf_exempt
def app_get_product_details(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        productId = request.POST.get('productId')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Product.objects.get(id=productId)
                if data:
                    # Serialize the data
                    dataSerializer = ProductSerializer(data, many=False)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_product_by_sku(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        productSku = request.POST.get('productSku')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Product.objects.filter(sku=productSku)
                if data:
                    # Serialize the data
                    dataSerializer = ProductSerializer(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_buyer_login(request):
    if request.method == "POST":
        try:
            securityKey = request.POST.get('securityKey')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            if securityKey != "!NARI!(^&*%@%!)":
                return JsonResponse({
                    'status': False,
                    'message': "Invalid security key."
                })

            # Fetch the buyer by phone
            try:
                buyer = Buyer.objects.get(phone=phone)
            except Buyer.DoesNotExist:
                return JsonResponse({
                    'status': False,
                    'message': "Invalid phone number or password."
                })

            # Check if the password is correct
            if not check_password(password, buyer.password):
                return JsonResponse({
                    'status': False,
                    'message': "Invalid phone number or password."
                })

            # Serialize the data
            dataSerializer = BuyerSerializer(buyer, many=False)

            # Return success response
            return JsonResponse({
                'status': True,
                'message': "Login successful.",
                'data': dataSerializer.data
            })

        except Exception as e:
            # Return error response if something goes wrong
            return JsonResponse({
                'status': False,
                'message': f"Error: {str(e)}"
            })

    return JsonResponse({
        'status': False,
        'message': "Invalid request method. Please use POST."
    })


@csrf_exempt
def app_buyer_register(request):
    if request.method == "POST":
        try:
            # Parse request data
            security_key = request.POST.get('securityKey')
            name = request.POST.get('name', '').strip()
            phone = request.POST.get('phone', '').strip()
            email = request.POST.get('email', '').strip()
            password = request.POST.get('password', '').strip()

            # Check security key
            if security_key != "!NARI!(^&*%@%!)":
                return JsonResponse({
                    'status': False,
                    'message': "Invalid security key."
                })

            # Validate required fields
            if not all([name, phone, email, password]):
                return JsonResponse({
                    'status': False,
                    'message': "All fields are required."
                })

            # Check if the phone number already exists
            if User.objects.filter(username=phone).exists():
                return JsonResponse({
                    'status': False,
                    'message': "Phone number already exists."
                })

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse({
                    'status': False,
                    'message': "Email already exists."
                })

            # Split name into first and last names
            first_name, last_name = name.split(" ", 1) if " " in name else (name, "")

            # Create Buyer instance
            buyer = Buyer(name=name, phone=phone, email=email, password=make_password(password))
            buyer.save()

            # Create User instance with hashed password
            user = User(
                username=phone,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password)  # Secure password storage
            )
            user.save()

            # Serialize buyer data
            data_serializer = BuyerSerializer(buyer, many=False)

            # Return success response
            return JsonResponse({
                'status': True,
                'message': "Registration successful.",
                'data': [data_serializer.data]
            })

        except Exception as e:
            # Handle unexpected errors
            return JsonResponse({
                'status': False,
                'message': f"An error occurred: {str(e)}"
            })
    else:
        return JsonResponse({
            'status': False,
            'message': "Invalid request method. Please use POST."
        })




@csrf_exempt
def app_add_address(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        userId = request.POST.get('userId')
        addressType = request.POST.get('addressType')
        alternatePhone = request.POST.get('alternatePhone')
        address = request.POST.get('address')
        landmark = request.POST.get('landmark')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                buyer = Buyer.objects.get(id=userId)
                if buyer:
                    newAdd=Address()
                    newAdd.buyer=buyer
                    newAdd.addressType=addressType
                    newAdd.alternatePhone=alternatePhone
                    newAdd.address=address
                    newAdd.landmark=landmark
                    newAdd.city=city
                    newAdd.state=state
                    newAdd.pin=pin
                    newAdd.save()

                    # Serialize the data
                    dataSerializer = AddressSerializers(newAdd, many=False)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_address(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        userId = request.POST.get('userId')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Address.objects.filter(buyer=Buyer.objects.get(id=userId))
                if data:
                    # Serialize the data
                    dataSerializer = AddressSerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })




@csrf_exempt
def app_add_wishlist(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        userId = request.POST.get('userId')
        productId = request.POST.get('productId')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                buyer = Buyer.objects.get(id=userId)
                product = Product.objects.get(id=productId)
                if buyer and product:
                    w=Wishlist()
                    w.buyer=buyer
                    w.product=product
                    w.save()
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Product added in wishlist successfully..."
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_wishlist(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        userId = request.POST.get('userId')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Wishlist.objects.filter(buyer=Buyer.objects.get(id=userId))
                if data:
                    # Serialize the data
                    dataSerializer = WishlistSerializers(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })


@csrf_exempt
def app_delete_wishlist(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        wishlistId = request.POST.get('wishlistId')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Wishlist.objects.get(id=wishlistId)
                if data:
                    data.delete()
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data deleted successfully...",
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })




@csrf_exempt
def app_add_order(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        userId = request.POST.get('userId')
        productId = request.POST.get('productId')
        addressId = request.POST.get('addressId')
        
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                buyer = Buyer.objects.get(id=userId)
                product = Product.objects.get(id=productId)
                address = Address.objects.get(id=addressId)
                if buyer and product:
                    newOrder=Order()
                    newOrder.buyer=buyer
                    newOrder.product=product
                    newOrder.address=address
                    newOrder.quantity=request.POST.get('quantity')
                    newOrder.totalPrice=request.POST.get('totalPrice')
                    newOrder.shippingPrice=request.POST.get('shippingPrice')
                    newOrder.finalPrice=request.POST.get('finalPrice')
                    newOrder.transactionId=request.POST.get('transactionId')
                    newOrder.save()
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Order added successfully..."
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })



@csrf_exempt
def app_get_order(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        userId = request.POST.get('userId')
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                data = Order.objects.filter(buyer=Buyer.objects.get(id=userId))
                if data:
                    # Serialize the data
                    dataSerializer = OrderSerializer(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "Data not found..."
                    })
            except Exception as e:
                # Return error response if something goes wrong
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })




@csrf_exempt
def app_search_product(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        query = request.POST.get('query', '').strip()
        
        if securityKey == "!NARI!(^&*%@%!)":
            try:
                # Filter products based on the search query
                data = Product.objects.filter(
                    Q(name__icontains=query) |  # Search by name
                    Q(description__icontains=query) |  # Search by description
                    Q(category__name__icontains=query) |  # Search by category name
                    Q(subcategory__name__icontains=query)  # Search by subcategory name
                ).distinct()  # Avoid duplicate results if multiple fields match
                
                if data.exists():
                    # Serialize the data
                    dataSerializer = ProductSerializer(data, many=True)
                    # Return success response
                    return JsonResponse({
                        'status': True,
                        'message': "Data found successfully...",
                        'data': dataSerializer.data
                    })
                else:
                    # Return not found response
                    return JsonResponse({
                        'status': False,
                        'message': "No products matched your search."
                    })
            except Exception as e:
                # Handle any errors
                return JsonResponse({
                    'status': False,
                    'message': f"Error: {str(e)}"
                })
        else:
            return JsonResponse({
                'status': False,
                'message': "Invalid security key."
            })
    else:
        return JsonResponse({
            'status': False,
            'message': "Only POST requests are allowed."
        })


