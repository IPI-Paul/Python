from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Product
from .serializers import ProductSerializer


# Django Rest Framework Generics RetrieveAPIView
class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()

@authentication_classes([])
@permission_classes([])
class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def perform_create(self, serializer):
    if(self.request.data['view'] == '02'):
      self.perform_create_02(serializer)
    elif(self.request.data['view'] == '03'):
      self.perform_create_03(serializer)
    elif(self.request.data['view'] == '04'):
      self.perform_create_04(serializer)

  def perform_create_02(self, serializer):
    print(serializer.validated_data)
    serializer.save()

  def perform_create_03(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)
    # send a Django signal

  def perform_create_04(self, serializer):
    serializer.save(user=self.request.user)
    print(serializer.validated_data)

product_create_view = ProductCreateAPIView.as_view()
