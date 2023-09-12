# Django Model Instance as an API Response

import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products_01.models import Product

def api_home_01(request, *args, **kwargs):
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  if model_data:
    # serialization : takes a model instance (model_data)
    # turns it in to a Python dict
    # and returns JSON to the client
    data['id'] = model_data.id
    data['title'] = model_data.title
    data['content'] = model_data.content
    data['price'] = model_data.price
  return JsonResponse(data)

def api_home_02(request, *args, **kwargs):
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  if model_data:
    data = model_to_dict(model_data, fields=['id', 'title', 'price'])
  return JsonResponse(data)

def api_home_03(request, *args, **kwargs):
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  if model_data:
    data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    data['price'] = str(data['price'])
    json_data_str = json.dumps(data)
  return HttpResponse(json_data_str, headers={'content-type': 'application/json'})