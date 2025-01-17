from django.db import models
from tinymce.models import HTMLField

class Supercategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.URLField(max_length=1024)
    def __str__(self):
        return self.name
    

class Maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.URLField(max_length=1024)
    title=models.CharField(max_length=100,default='',null=True,blank=True)
    description=models.TextField(default='',null=True,blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    maincategory = models.ForeignKey(Maincategory, on_delete=models.DO_NOTHING, related_name="categories")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.URLField(max_length=1024)
    specifications = models.JSONField(default=dict)  # Requires Django 3.1+
    title=models.CharField(max_length=100,default='',null=True,blank=True)
    description=models.TextField(default='',null=True,blank=True)
    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="subcategories")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.URLField(max_length=1024)
    title=models.CharField(max_length=100,default='',null=True,blank=True)
    description=models.TextField(default='',null=True,blank=True)
    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.URLField(max_length=1024)
    title=models.CharField(max_length=100,default='',null=True,blank=True)
    description=models.TextField(default='',null=True,blank=True)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    
class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    offers=models.ForeignKey(Supercategory,on_delete=models.DO_NOTHING,related_name="offers",default='',null=True,blank=True)
    maincategory=models.ForeignKey(Maincategory,on_delete=models.DO_NOTHING,related_name="maincategory")
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name="categories")
    subcategory=models.ForeignKey(Subcategory,on_delete=models.DO_NOTHING,related_name="subcategories")
    brand=models.ForeignKey(Brand,on_delete=models.DO_NOTHING,related_name="brands")
    image1 = models.URLField(max_length=1024)
    image2= models.URLField(max_length=1024)
    image3= models.URLField(max_length=1024)
    image4= models.URLField(max_length=1024)
    name=models.CharField(max_length=300)
    base_price=models.FloatField(default=0,null=True,blank=True)
    discount=models.FloatField(default=0,null=True,blank=True)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    size=models.CharField(max_length=300)
    color=models.CharField(max_length=300)
    specifications = models.JSONField(default=dict)
    rating=models.FloatField(default=0,null=True,blank=True)
    reviews=models.IntegerField(default=0,null=True,blank=True)

    #delhivery details
    weight=models.IntegerField(default=0,null=True,blank=True)
    length=models.FloatField(default=0,null=True,blank=True)
    height=models.FloatField(default=0,null=True,blank=True)
    width=models.FloatField(default=0,null=True,blank=True)
    #discount
    tax=models.FloatField(default=18,null=True,blank=True)

    description=models.TextField()
    faq = models.JSONField(default=dict)
    sku=models.CharField(max_length=200,default='',null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    


class Blog(models.Model):
    id=models.AutoField(primary_key=True)
    image = models.URLField(max_length=1024)
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    description=HTMLField(default='')
    meta_description=models.TextField(default='',null=True,blank=True)
    views=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title