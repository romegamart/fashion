#API
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *

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



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .serializers import ProductSerializer

@csrf_exempt
def app_get_product(request):
    if request.method == "POST":
        securityKey = request.POST.get('securityKey')
        if securityKey != "!NARI!(^&*%@%!)":
            return JsonResponse({'status': False, 'message': "Invalid security key."})
        
        # Extract values for filtering
        selected_maincategories = request.POST.getlist('maincategory[]')
        selected_categories = request.POST.getlist('category[]')
        selected_subcategories = request.POST.getlist('subcategory[]')
        selected_brands = request.POST.getlist('brand[]')
        selected_colors = request.POST.getlist('color[]')
        selected_size = request.POST.get('size')

        try:
            # Start filtering based on values (not IDs)
            data = Product.objects.all()

            if selected_maincategories:
                data = data.filter(maincategory__name__in=selected_maincategories)
            if selected_categories:
                data = data.filter(category__name__in=selected_categories)
            if selected_subcategories:
                data = data.filter(subcategory__name__in=selected_subcategories)
            if selected_brands:
                data = data.filter(brand__name__in=selected_brands)
            if selected_colors:
                data = data.filter(color__in=selected_colors)
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
