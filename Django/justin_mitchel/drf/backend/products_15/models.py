# Django Model Instance as an API Response =>
from django.db import models
# <= Django Model Instance as an API Response
# Request User Data and Customize View Queryset => 
from django.conf import settings
from os.path import sep

name = __file__.split(sep)[-2]
# <= Request User Data and Customize View Queryset


# Request User Data and Customize View Queryset => 
# Using auth.User
User = settings.AUTH_USER_MODEL
# <= Request User Data and Customize View Queryset

class Product(models.Model):
  # pk
  # Request User Data and Customize View Queryset =>
  user = models.ForeignKey(
    User, 
    default=1, 
    null=True, 
    on_delete=models.SET_NULL, 
    related_name=name
  )
  # <= Request User Data and Customize View Queryset
  # Django Model Instance as an API Response =>
  title = models.CharField(max_length=120)
  content = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
  # <= Django Model Instance as an API Response

  # REST framework model serializers =>
  @property
  def sale_price(self):
    return "%.2f" %(float(self.price) * 0.8)

  def get_discount(self):
    return '122'
  # <= REST framework model serializers