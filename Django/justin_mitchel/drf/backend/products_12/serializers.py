# Django Rest Framework Model Serializers =>
from rest_framework import serializers
from .models import Product
# <= Django Rest Framework Model Serializers
# URLS, Reverse & Serializers =>
from rest_framework.reverse import reverse
from api_06.serializers import ViewNameSerializer, get_detail_name
# <= URLS, Reverse & Serializers


class ProductSerializer(serializers.ModelSerializer):
  # URLS, Reverse & Serializers =>
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['url'] = ViewNameSerializer(*args, **kwargs).__dict__['fields']['url']
  # <= URLS, Reverse & Serializers
  
  # Django Rest Framework Model Serializers =>
  discount = serializers.SerializerMethodField(read_only=True)
  # <= Django Rest Framework Model Serializers
  # URLS, Reverse & Serializers =>
  edit_url = serializers.SerializerMethodField(read_only=True)
  url = serializers.CharField(read_only=True)
  # <= URLS, Reverse & Serializers

  class Meta:
    model = Product
    fields = [
      'url',
      'edit_url',
      'pk',
      'title',
      'content',
      'price',
      'sale_price',
      'discount'
    ]

  # Custom Validation With Serializers =>
  def validate_title(self, value):
    # qs = Product.objects.filter(title__exact=value)
    qs = Product.objects.filter(title__iexact=value) # case insensitive
    if qs.exists():
      raise serializers.ValidationError(f"{value} is already a product name.")
    return value
  # <= Custom Validation With Serializers
  
  # URLS, Reverse & Serializers =>
  def get_edit_url(self, obj):
    request = self.context.get('request')
    # if request is None:
    #   return None
    resolver = self.get_resolver()
    url_name = resolver.__dict__['url_name']
    url = ''
    if 'pk' in obj.__dict__:
      url = reverse(f'{url_name}', kwargs={'pk': obj.pk}, request=request) 
    elif 'kwargs' in resolver.__dict__ and 'pk' in resolver.__dict__['kwargs'] and \
        'detail' in url_name:
      url = reverse(f'{url_name}', kwargs={'pk': obj.id}, request=request) 
    else:
      try:
        url = reverse(f'{url_name}', request=request)
        if len(url.split('/')) > 0 and url.split('/')[-1] != obj.id:
          url += str(obj.id)
      except:
        url_name = get_detail_name(url_name)
        if url_name is not None:
          url = reverse(f'{url_name}', kwargs={'pk': obj.id}, request=request)
    return url
  
  def get_resolver(self):
    request = self.context.get('request')
    _ = request.__dict__['parser_context']['request'].__dict__['_request']
    return _.__dict__['resolver_match']
  # <= URLS, Reverse & Serializers
  
  # Django Rest Framework Model Serializers =>
  def get_discount(self, obj):
    if not hasattr(obj, 'id'):
      return None
    if not isinstance(obj, Product):
      return None
    return obj.get_discount()
  # <= Django Rest Framework Model Serializers