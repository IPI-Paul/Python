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
  #URLS, Reverse & Serializers =>
  edit_url = serializers.SerializerMethodField(read_only=True)
  url = serializers.CharField(read_only=True)
  # <= #URLS, Reverse & Serializers
  # Model Serializer Create & Update Methods => 
  email = serializers.EmailField(write_only=True)
  # <= Model Serializer Create & Update Methods

  class Meta:
    model = Product
    fields = [
      'url',
      'edit_url',
      'email',
      'pk',
      'title',
      'content',
      'price',
      'sale_price',
      'discount'
    ]

  # Model Serializer Create & Update Methods => 
  # Can also be done in the perform_create method of the View itself
  def create(self, validated_data):
	#   # return Product.objects.create(**validated_data) 
  #   # or
    email = validated_data.pop('email')
    obj = super().create(validated_data)
    # print(email, obj, '\n', {**validated_data})
    return obj

  # perform_create in the View itself calls the following Serializer method when 
  # calling serializer.save(content=content) 
  def update(self, instance, validated_data):
    email = validated_data.pop('email')
    if email:
      return super().update(instance, validated_data)
    instance.title = validated_data.get('title')
    return instance
  # <= Model Serializer Create & Update Methods
  
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