from rest_framework import serializers
import re
import inspect
import sys


# URLS, Reverse & Serializers =>
def get_detail_name(view_name):
  url_name = re.match('api_[0-9]+_products_[0-9]+', view_name)[0]
  product_name = re.match('.*(products_[0-9]+)', view_name).group(1)
  _ = [
    x.name for x in [
      x for _, x in inspect.getmembers(sys.modules[f'{product_name}.urls']) 
      if _ == 'urlpatterns'
    ][0]
    if 'detail' in x.__dict__['name']
  ]
  if len(_) > 0:
    return _[0]
  return None

class ViewNameSerializer(serializers.Serializer):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    request = self.context.get('request')
    if request:
      _ = request.__dict__['parser_context']['request'].__dict__['_request']
      resolver = _.__dict__['resolver_match']
      view_name = resolver.__dict__['url_name']
      if 'kwargs' in resolver.__dict__ and 'pk' in resolver.__dict__['kwargs'] and \
          'detail' in view_name:
        url = serializers.HyperlinkedIdentityField(
          view_name=view_name,
          lookup_field='pk'
        )
        self.fields['url'] = url
      else:
        url_name = re.match('api_[0-9]+_products_[0-9]+', view_name)[0]
        product_name = re.match('.*(products_[0-9]+)', view_name).group(1)
        _ = [
          x.name for x in [
            x for _, x in inspect.getmembers(sys.modules[f'{product_name}.urls']) 
            if _ == 'urlpatterns'
          ][0]
          if 'detail' in x.__dict__['name']
        ]
        if len(_) > 0:
          view_name = _[0]
          url = serializers.HyperlinkedIdentityField(
            view_name=view_name,
            lookup_field='pk'
          )
          self.fields['url'] = url
    elif 'source' in kwargs:
      product_name = re.match('.*(products_[0-9]+)', kwargs['source']).group(1)
      urls = [
        x for _, x in inspect.getmembers(sys.modules[f'{product_name}.urls']) 
        if _ == 'urlpatterns'
      ]
      if len(urls) > 0:
        _ = [x.name for x in urls[0] if 'detail' in x.__dict__['name']]
        if len(_) > 0:
          view_name = _[0]
          url = serializers.HyperlinkedIdentityField(
            view_name=view_name,
            lookup_field='pk'
          )
          self.fields['url'] = url
      
  url = serializers.CharField(read_only=True)
# <= URLS, Reverse & Serializers

# Pagination => 
class UserPracticalPublicSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  username = serializers.CharField(read_only=True)
# <= Pagination

# Related Fields and Foreign Key Serializer =>  
class UserPublicSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  username = serializers.CharField(read_only=True)
  other_products = serializers.SerializerMethodField(read_only=True)

  def get_other_products(self, obj):
    request = self.context.get('request')
    user = obj
    # my_products_qs = user.product_set.all()[:5]
    my_products_qs = user.products_17.all()[:5]
    return UserProductInlineSerializer(
      my_products_qs, many=True, context=self.context
    ).data


class UserProductInlineSerializer(serializers.Serializer):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['url'] = ViewNameSerializer(*args, **kwargs).__dict__['fields']['url']
      
  url = serializers.CharField(read_only=True)
  title = serializers.CharField(read_only=True)  
  pk = serializers.CharField(read_only=True) 
  # <= Related Fields and Foreign Key Serializer