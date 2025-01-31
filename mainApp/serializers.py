from rest_framework import serializers
from .models import *




class SliderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'category', 'image']

    def create(self, validated_data):
        return Slider.objects.create(**validated_data)


class SupercategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Supercategory
        fields = ['id', 'name', 'slug', 'image','background_image']

    def create(self, validated_data):
        return Supercategory.objects.create(**validated_data)


class MaincategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Maincategory
        fields = ['id', 'name', 'slug', 'image']

    def create(self, validated_data):
        return Maincategory.objects.create(**validated_data)


class CategorySerializers(serializers.ModelSerializer):
    maincategory = serializers.SlugRelatedField(
        queryset=Maincategory.objects.all(),
        slug_field='slug'  # Field to use instead of the ID
    )

    class Meta:
        model = Category
        fields = ['id', 'maincategory', 'name', 'slug', 'image', 'app_background', 'specifications']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class SubcategorySerializers(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name')
    class Meta:
        model=Subcategory
        fields=['id','category','name','slug','image']

    def create(self, validated_data):
        return Subcategory.objects.create(**validated_data)

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=['id','name','slug','image']
    
    def create(self, validated_data):
        return Brand.objects.create(*validated_data)
    

class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=['id','name']
    
    def create(self, validated_data):
        return Color.objects.create(*validated_data)
    

class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Size
        fields=['id','name']
    
    def create(self, validated_data):
        return Size.objects.create(*validated_data)



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'offers','maincategory', 'category', 'subcategory', 'brand', 
            'image1', 'image2', 'image3', 'image4', 
            'name', 'base_price', 'discount', 'price', 
            'quantity', 'size', 'color', 'specifications', 
            'rating', 'reviews', 'weight', 'length', 
            'height', 'width', 'tax', 'description', 
            'faq', 'sku', 'date'
        ]
        depth = 1

    def create(self, validated_data):
        return Product.objects.create(*validated_data)



class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'name', 'phone', 'email', 'verification', 'date']


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'buyer', 'addressType', 'alternatePhone', 'address', 'landmark', 'city', 'state', 'pin']
        depth = 1


class WishlistSerializers(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = ['id', 'buyer', 'product']
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'buyer',
            'product',
            'address',
            'quantity',
            'totalPrice',
            'shippingPrice',
            'finalPrice',
            'transactionId'
        ]
        depth = 1

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
