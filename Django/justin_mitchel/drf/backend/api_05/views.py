# Injest Data with Django Rest Framework

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from products_03.models import Product
from products_03.serializers import ProductSerializer


def api_home_01(request, *args, **kwargs):
  """
  DRF API View
  """
  # data = request.data
  data = request.POST
  return JsonResponse(data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def api_home_02(request, *args, **kwargs):
  data = request.data
  return Response(data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def api_home_03(request, *args, **kwargs):
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    print(serializer.data)
    data = serializer.data
    return Response(data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def api_home_04(request, *args, **kwargs):
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    instance = serializer.save()
    # instance = form.save()
    print(instance)
    return Response(serializer.data)
  return Response({'invalid': 'Not good data'}, status=400)