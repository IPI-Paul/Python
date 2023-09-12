from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Session Authentication & Permissions
class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticated]
  # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)
    # send a Django signal

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductListCreateAPIView_01(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)
    # send a Django signal

product_list_create_view_01 = ProductListCreateAPIView_01.as_view()

class ProductListCreateAPIView_02(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  authentication_classes = [authentication.SessionAuthentication]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)
    # send a Django signal

product_list_create_view_02 = ProductListCreateAPIView_02.as_view()

# User & Group Permissions with DjangoModelPermissions

class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # Currently permissions only on one single view: ProductListCreateAPIView
  permission_classes = [permissions.DjangoModelPermissions] 
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.DjangoModelPermissions] 
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    # instance 
    super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()