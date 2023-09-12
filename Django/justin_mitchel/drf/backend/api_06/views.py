from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from products_03.models import Product
from products_03.serializers import ProductSerializer

# Django Rest Framework Generics RetrieveAPIView

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def api_home(request, *args, **kwargs):
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    instance = serializer.save()
    # instance = form.save()
    print(instance)
    return Response(serializer.data)
  return Response({'invalid': 'Not good data'}, status=400)

# Django Rest Framework Generics CreateAPIView
