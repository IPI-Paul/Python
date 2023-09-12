# Django Rest Framework Model Serializers =>
from rest_framework import serializers
from .models import Product
# <= Django Rest Framework Model Serializers
# URLS, Reverse & Serializers =>
from rest_framework.reverse import reverse
from api_06.serializers import ViewNameSerializer, get_detail_name
# <= URLS, Reverse & Serializers
# Custom Validation With Serializers =>
from . import validators
# <= Custom Validation With Serializers
# Pagination =>
from api_06.serializers import UserPracticalPublicSerializer
# <= Pagination


class ProductSerializer(serializers.ModelSerializer):
  # URLS, Reverse & Serializers =>
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # parser_context = kwargs['context']['request'].__dict__['parser_context']
    # request = parser_context['request'].__dict__['_request'].__dict__
    request = kwargs['context']['request'].__dict__['_request'].__dict__
    request['resolver_match'].__dict__['url_name'] = 'api_06_products_20'
    self.fields['url'] = ViewNameSerializer(*args, **kwargs).__dict__['fields']['url']
  # <= URLS, Reverse & Serializers
  # Custom Validation With Serializers =>
    if request['method'] == 'PUT':
      self.fields['title'] = serializers.CharField(
        validators=[validators.UpdateValidator()]
      )
  # <= Custom Validation With Serializers
  
  # URLS, Reverse & Serializers =>
  edit_url = serializers.SerializerMethodField(read_only=True)
  url = serializers.CharField(read_only=True)
  # <= URLS, Reverse & Serializers
  # Custom Validation With Serializers =>
  title = serializers.CharField(validators=[
    validators.validate_title_no_hello,
    validators.unique_product_title
    ])
  # <= Custom Validation With Serializers
  # Related Fields and Foreign Key Serializer =>
  # user = UserPublicSerializer(read_only=True)
  owner = UserPracticalPublicSerializer(source='user', read_only=True)
  # <= Related Fields and Foreign Key Serializer
  # Unified Design of Serializers & Indices =>
  body = serializers.CharField(source='content')
  # <= Unified Design of Serializers & Indices

  class Meta:
    model = Product
    fields = [
      'owner',
      'url',
      'edit_url',
      'pk',
      'title',
      'body',
      'price',
      'sale_price',
      'public',
      'path',
      'endpoint'
    ]

  
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