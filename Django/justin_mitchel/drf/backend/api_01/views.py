# Create your first API View

import json
from django.http import JsonResponse

def api_home_01(request, *args, **kwargs):
  return JsonResponse({"message": "Hi there, this is your Django API response!!"})

def api_home_02(request, *args, **kwargs):
  # request -> HttpRequest -> Django
  # print(dir(request))
  # request.body
  print(request.GET) # url query params
  print(request.POST)
  body = request.body # byte string of JSON data
  data = {}
  try:
    data = json.loads(body)
  except:
    pass
  print(data)
  # data['headers'] = request.headers # request.META ->
  data['params'] = dict(request.GET)
  data['headers'] = dict(request.headers) # request.META ->
  print(request.headers)
  data['content_type'] = request.content_type
  return JsonResponse(data)