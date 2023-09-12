from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from api_06.mixins import (
  StaffEditorPermissionMixin,
  UserQuerySetMixin
)

# Django Rest Framework Using Mixins for Permissions

class ProductDetailAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.RetrieveAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()

class ProductListCreateAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.ListCreateAPIView
):
  "Text here appears in Django pages, but can't be dynamic!"
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    #Request User Data and Customize View Queryset =>
    request = self.request
    serializer.save(user=request.user, content=content)
    # <= Request User Data and Customize View Queryset
    # send a Django signal

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductUpdateAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.UpdateAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
  UserQuerySetMixin,
  StaffEditorPermissionMixin,
  generics.DestroyAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  def perform_destroy(self, instance):
    # instance 
    super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()