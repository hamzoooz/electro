from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User   
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=25)
    image1 = models.ImageField(upload_to='products/images')
    description = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}"
 
    
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images', null=True, blank=True)
    bio = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"
  
    
class Product(models.Model):
    title = models.CharField(max_length=25)
    image1 = models.ImageField(upload_to='products/images' , null=True, blank=True)
    image2 = models.ImageField(upload_to='products/images' , null=True, blank=True)
    image3 = models.ImageField(upload_to='products/images' , null=True, blank=True)
    image4 = models.ImageField(upload_to='products/images' , null=True, blank=True)
    image5 = models.ImageField(upload_to='products/images' , null=True, blank=True)
    orignal_price = models.FloatField()
    selling_proce = models.FloatField()
    status = models.CharField(max_length=10)
    discond = models.IntegerField()
    description = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"
    
