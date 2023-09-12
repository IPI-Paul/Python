from rest_framework import generics
from products_19.models import Product as Product_19
from products_19.serializers import ProductSerializer as ProductSerializer_19
from products_20.models import Product as Product_20
from products_20.serializers import ProductSerializer as ProductSerializer_20


class SearchListView19(generics.ListAPIView):
  queryset = Product_19.objects.all()
  serializer_class = ProductSerializer_19

  def get_queryset(self, *args, **kwargs):
    qs = super().get_queryset(*args, **kwargs)
    q = self.request.GET.get('q')
    results = Product_19.objects.none()
    if q is not None:
      user = None
      if self.request.user.is_authenticated:
        user = self.request.user
      results = qs.search(q, user=user)
    return results

class SearchListView20(generics.ListAPIView):
  queryset = Product_20.objects.all()
  serializer_class = ProductSerializer_20

  def get_queryset(self, *args, **kwargs):
    qs = super().get_queryset(*args, **kwargs)
    q = self.request.GET.get('q')
    results = Product_20.objects.none()
    if q is not None:
      user = None
      if self.request.user.is_authenticated:
        user = self.request.user
      results = qs.search(q, user=user)
    return results