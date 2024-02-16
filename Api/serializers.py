from rest_framework.serializers import ModelSerializer
from main import models


class ListProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id',]

class ListCategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class ListEnterSerializer(ModelSerializer):
    class Meta:
        model = models.EnterProduct
        fields = '__all__'

class ListChiqimSerializer(ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'