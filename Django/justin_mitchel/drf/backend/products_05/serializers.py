# Django Rest Framework Model Serializers =>
from rest_framework import serializers
from .models import Product
# <= Django Rest Framework Model Serializers


class ProductSerializer(serializers.ModelSerializer):
  # Django Rest Framework Model Serializers =>
  discount = serializers.SerializerMethodField(read_only=True)
  # <= Django Rest Framework Model Serializers
  class Meta:
    model = Product
    fields = [
      'title',
      'content',
      'price',
      'sale_price',
      'discount'
    ]
  
  # Django Rest Framework Model Serializers =>
  def get_discount(self, obj):
    if not hasattr(obj, 'id'):
      return None
    if not isinstance(obj, Product):
      return None
    return obj.get_discount()
  # <= Django Rest Framework Model Serializers