
from django.contrib import admin
from django.urls import path
from mainApp import views
from mainApp import backend
from mainApp import api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('search/',views.search_product),
    path('men/',views.men_home_page),
    path('kid/',views.kid_home_page),
    path('offers/<str:cat>/',views.offers_page),
    path('product/<str:cat>/',views.product_page),
    path('category/<str:cat>/',views.category_page),
    path('product-details/<str:name>-<int:id>/',views.product_detail),
    # path('dynamic-filter/',views.dynamic_filter),
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
    path('login/',views.login_page),
    path('logout/',views.logout_page),
    path('register/',views.register),
    path('my-account/',views.my_account),
    path('my-account-address/',views.my_account_address),
    path('my-account-edit/',views.my_account_edit),
    path('my-account-orders/',views.my_account_order),
    path('my-account-orders-details/',views.my_account_order_details),
    path('order-tracking/',views.order_tracking),
    path('payment-confirmation/',views.payment_confirmation),
    path('payment-failure/',views.payment_failure),

    #Backend
    #Image Upload
    path('prduct-store/',backend.product_store),
    path('admin-login/',backend.admin_login),
    path('admin-dashboard/',backend.admin_dashboard),


    #Slider
    path('slider/',backend.slider_page),
    path('delete-slider/<int:id>/',backend.delete_slider),

    #Maincategory
    path('supercategory/',backend.supercategory_page),
    path('add-supercategory/',backend.add_supercategory),
    path('update-supercategory/<int:id>/',backend.update_supercategory),
    path('delete-supercategory/<int:id>/',backend.delete_supercategory),

    #Maincategory
    path('maincategory/',backend.maincategory_page),
    path('add-maincategory/',backend.add_maincategory),
    path('update-maincategory/<int:id>/',backend.update_maincategory),
    path('delete-maincategory/<int:id>/',backend.delete_maincategory),

    #Category
    path('category/',backend.category_page),
    path('add-category/',backend.add_category),
    path('update-category/<int:id>/',backend.update_category),
    path('delete-category/<int:id>/',backend.delete_category),

    #Subcategory
    path('subcategory/',backend.subcategory_page),
    path('add-subcategory/',backend.add_subcategory),
    path('update-subcategory/<int:id>/',backend.update_subcategory),
    path('delete-subcategory/<int:id>/',backend.delete_subcategory),
    
    #Brand
    path('brand/',backend.brand_page),
    path('add-brand/',backend.add_brand),
    path('update-brand/<int:id>/',backend.update_brand),
    path('delete-brand/<int:id>/',backend.delete_brand),
    
    #Color
    path('color/',backend.color_page),
    path('add-color/',backend.add_color),
    path('update-color/<int:id>/',backend.update_color),
    path('delete-color/<int:id>/',backend.delete_color),
    
    #Color
    path('size/',backend.size_page),
    path('add-size/',backend.add_size),
    path('update-size/<int:id>/',backend.update_size),
    path('delete-size/<int:id>/',backend.delete_size),
    
    #Product
    path('product/',backend.product_page),
    path('add-product/',backend.add_product),
    path('update-product/<int:id>/<int:pn>/',backend.update_product),
    path('duplicate-product/<int:id>/<int:pn>/',backend.duplicate_product),
    path('delete-product/<int:id>/',backend.delete_product),
    #updating offers
    path('update-product-offers/<int:id>/<str:ops>/',backend.update_product_offers),

    #API Start Here
    path('app-get-offers/',api.app_get_offers),
    path('app-get-maincategory/',api.app_get_maincategory),
    path('app-get-category/',api.app_get_category),
    path('app-get-subcategory/',api.app_get_subcategory),
    path('app-get-brand/',api.app_get_brand),
    path('app-get-color/',api.app_get_color),
    path('app-get-size/',api.app_get_size),
    path('app-get-product/',api.app_get_product),
    path('app-get-product-details/',api.app_get_product_details),
    path('app-get-product-by-sku/',api.app_get_product_by_sku),
    path('app-get-slider/',api.app_get_slider),
    path('app-buyer-login/',api.app_buyer_login),
    path('app-buyer-register/',api.app_buyer_register),
    #address
    path('app-add-address/',api.app_add_address),
    path('app-get-address/',api.app_get_address),
    #wishlist
    path('app-add-wishlist/',api.app_add_wishlist),
    path('app-get-wishlist/',api.app_get_wishlist),
    path('app-delete-wishlist/',api.app_delete_wishlist),
    #order
    path('app-add-order/',api.app_add_order),
    path('app-get-order/',api.app_get_order),
    path('app-search-product/',api.app_search_product),


    #Front end main operation
    path('<str:mcat>/<str:cat>/',views.product_by_maincategory_category),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

