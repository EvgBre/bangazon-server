from django.db import models
from .user import User
from .payment_type import PaymentType

class Order(models.Model):
  
  customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
  date_placed = models.DateField()
  payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
  total = models.DecimalField(max_digits=7, decimal_places=2)
  is_completed = models.BooleanField()
