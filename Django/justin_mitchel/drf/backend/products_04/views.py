from rest_framework import generics, mixins
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Product
from .serializers import ProductSerializer


# Django Rest Framework Generics LisAPIView & ListCreateAPIView
class ProductListAPIView(generics.ListAPIView):
  # Not gonna use this method
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk'

product_list_view = ProductListAPIView.as_view()

@authentication_classes([])
@permission_classes([])
class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    # print(serializer.validated_data)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(content=content)
    # send a Django signal

product_list_create_view = ProductListCreateAPIView.as_view()

# Using Function Based Views For Create Retrieve or List
@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def product_alt_view_01(request, pk=None, *args, **kwargs):
  method = request.method # PUT -> UPDATE -> DESTROY -> DELETE (CRUD)

  if method == 'GET':
    if pk is not None:
      # detail view
      queryset = Product.objects.filter(pk=pk)
      if not queryset.exists():
        raise Http404
      data = ProductSerializer(queryset, many=True).data
      return Response(data)
      # list view
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response(data)

  if method == 'POST':
    # create an item
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content')
      if content is None:
        content = title
      serializer.save(content=content)
      return Response(serializer.data)
    return Response({'invalid': 'Not good data'}, status=400)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def product_alt_view_02(request, pk=None, *args, **kwargs):
  method = request.method # PUT -> UPDATE -> DESTROY -> DELETE (CRUD)

  if method == 'GET':
    if pk is not None:
      # detail view
      obj = get_object_or_404(Product, pk=pk)
      data = ProductSerializer(obj, many=False).data
      return Response(data)
      # list view
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response(data)

  if method == 'POST':
    # create an item
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content') or None
      if content is None:
        content = title
      serializer.save(content=content)
      return Response(serializer.data)
    return Response({'invalid': 'Not good data'}, status=400)

# UpdateAPIView & DestroyAPIView

@authentication_classes([])
@permission_classes([])
class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

@authentication_classes([])
@permission_classes([])
class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    # instance 
    super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()

# Mixins and a Generic API View

@authentication_classes([])
@permission_classes([])
class ProductMixinView(
  mixins.CreateModelMixin, 
  mixins.ListModelMixin, 
  mixins.RetrieveModelMixin, 
  generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def get(self, request, *args, **kwargs): # http method GET
    # print(args, kwargs)
    pk = kwargs.get('pk')
    if pk is not None:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  # not required but can also include  
  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = 'This is a single view doing cool stuff!'
    serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()
