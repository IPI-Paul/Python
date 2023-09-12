# Django Model Instance as an API Response =>
from django.db import models
# <= Django Model Instance as an API Response
# Request User Data and Customize View Queryset => 
from django.conf import settings
from os.path import sep
# A Django Based Search for our Product API =>
from django.db.models import Q
# <= A Django Based Search for our Product API

name = __file__.split(sep)[-2]
# <= Request User Data and Customize View Queryset


# Request User Data and Customize View Queryset => 
# Using auth.User
User = settings.AUTH_USER_MODEL
# <= Request User Data and Customize View Queryset

# A Django Based Search for our Product API =>
class ProductQuerySet(models.QuerySet):
  def is_public(self):
    return self.filter(public=True)
  
  def search(self, query, user=None):
    lookup = Q(title__icontains=query) | Q(content__icontains=query)
    qs = self.is_public().filter(lookup)
    if user is not None:
      qs2 = self.filter(user=user).filter(lookup)
      qs = (qs | qs2).distinct()
    return qs

class ProductManager(models.Manager):
  def get_queryset(self, *args, **kwargs):
    return ProductQuerySet(self.model, using=self._db)

  def search(self, query, user=None):
    # return Product.objects.filter(public=True).filter(title__icontains=query)
    return self.get_queryset().search(query, user=user)
# <= A Django Based Search for our Product API

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
  # A Django Based Search for our Product API =>
  public = models.BooleanField(default=True)
  objects = ProductManager()
  # <= A Django Based Search for our Product API

  # REST framework model serializers =>
  @property
  def sale_price(self):
    return "%.2f" %(float(self.price) * 0.8)

  def get_discount(self):
    return '122'
  # <= REST framework model serializers