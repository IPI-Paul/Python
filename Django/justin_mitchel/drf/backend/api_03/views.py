# Rest Framework View & Response

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from products_01.models import Product

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def api_home_01(request, *args, **kwargs):
  """
  DRF API View
  """
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  if model_data:
    data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
  return Response(data)

@api_view(["GET", "POST"])
@authentication_classes([])
@permission_classes([])
def api_home_02(request, *args, **kwargs):
  """
  DRF API View
  """
  if request.method != "POST":
    return Response({"detail": "GET not allowed!"}, status=405)
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  if model_data:
    data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
  return Response(data)