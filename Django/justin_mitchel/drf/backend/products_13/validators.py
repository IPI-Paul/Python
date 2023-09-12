from rest_framework import serializers
from .models import Product

def validate_title(value):
  # qs = Product.objects.filter(title__exact=value)
  qs = Product.objects.filter(title__iexact=value) # case insensitive
  if qs.exists():
    raise serializers.ValidationError(f"{value} is already a product name.")
  return value

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