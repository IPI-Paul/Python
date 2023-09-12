from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission
from api_06.authentication import TokenAuthentication


# Django Rest Framework Token Authentication

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk'
  authentication_classes = [
    authentication.SessionAuthentication,
    TokenAuthentication
  ]
  permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

product_detail_view = ProductDetailAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  authentication_classes = [
    authentication.SessionAuthentication,
    TokenAuthentication
  ]
  permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)
    # send a Django signal

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  authentication_classes = [
    authentication.SessionAuthentication,
    TokenAuthentication
  ]
  permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  authentication_classes = [
    authentication.SessionAuthentication,
    TokenAuthentication
  ]
  permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

  def perform_destroy(self, instance):
    # instance 
    super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()