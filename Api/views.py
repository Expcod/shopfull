from main import models
from Api import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_products(request):
    products = models.Product.objects.all()
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categorys = models.Category.objects.all()
    serializer = serializers.ListCategorySerializer(categorys, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def enter_list(request):
    enters = models.EnterProduct.objects.all()
    serializer = serializers.ListEnterSerializer(enters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def expenditure(request):
    cartproducts = models.CartProduct.objects.filter(card__is_active=False)
    serializer = serializers.ListChiqimSerializer(cartproducts, many=True)
    return Response(serializer.data)
    