from main import models
from rest_framework import serializers

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id',]

class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class ListEnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnterProduct
        fields = '__all__'

class ListChiqimSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'


class DetailProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = models.Product
        depth = 1
        fields = ['id', 'name', 'description', 
                  'quantity', 'price', 'currency', 
                  'discount_price', 'baner_image', 
                  'category', 'review', 'is_discount', 
                  'is_active' ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'