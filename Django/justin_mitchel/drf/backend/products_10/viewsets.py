from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  '''
  Method Functions:
  get -> list -> Queryset
  get -> retrieve -> Product Instance Detail View
  post -> create -> New Instance
  post -> Update
  patch -> Partial Update
  delete -> destroy
  '''
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk' # default


class ProductGenericViewSet(
  mixins.ListModelMixin, 
  mixins.RetrieveModelMixin, 
  viewsets.GenericViewSet):
  '''
  Method Functions:
  get -> list -> Queryset
  get -> retrieve -> Product Instance Detail View
  '''
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk' # default

# Can't be registered with rest_framework.routers DefaultRouter
product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})