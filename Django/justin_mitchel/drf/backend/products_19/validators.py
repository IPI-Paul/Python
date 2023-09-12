from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

def validate_title_no_hello(value):
  if 'hello' in value.lower():
    raise serializers.ValidationError(f"{value} is not allowed")
  return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')

class UpdateValidator:
  requires_context = True

  def __call__(self, value, serializer_field):
    instance = getattr(serializer_field.parent, 'instance', None)
    if value == '':
      raise serializers.ValidationError(f"Error: Empty value is not allowed")
    elif instance and value not in instance.title:
      excl_pk = Product.objects.exclude(pk=instance.pk)
      if len([x for x in excl_pk if value.lower() == x.title.lower()]):
        raise serializers.ValidationError(f"Error: {value} already exists")
    return value