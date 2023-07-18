from django.db import models
from .user import User
from .category import Category


class Product(models.Model):
  
  name = models.CharField(max_length=300)
  seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.CharField(max_length=1000)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  quantity = models.IntegerField()
  product_image_url = models.CharField(max_length=5000)
  added_on = models.DateField()
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)