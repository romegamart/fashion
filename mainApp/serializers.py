from rest_framework import serializers
from .models import *


class SupercategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Supercategory
        fields = ['id', 'name', 'slug', 'image']

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
        fields = ['id', 'maincategory', 'name', 'slug', 'image', 'specifications']

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
    maincategory = serializers.SlugRelatedField(
        queryset=Maincategory.objects.all(),
        slug_field='name'  # Assuming 'name' is the field you want to display
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )
    subcategory = serializers.SlugRelatedField(
        queryset=Subcategory.objects.all(),
        slug_field='name'
    )
    brand = serializers.SlugRelatedField(
        queryset=Brand.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = [
            'id', 'maincategory', 'category', 'subcategory', 'brand', 
            'image1', 'image2', 'image3', 'image4', 
            'name', 'price', 'quantity', 'size', 'color', 
            'specifications', 'rating', 'reviews', 'description', 
            'faq', 'sku', 'date'
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
   