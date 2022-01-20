from rest_framework import serializers
from .models import Category
from .models import Tag
from .models import Product
from .models import Review
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'is_active']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'value']


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField
    reviews = serializers.SerializerMethodField

    class Meta:
        model = Product
        fields = ['id', 'title', 'tags', 'price', 'category', 'description']


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'reviews']

    def get_reviews(self, product):
        rate = Review.objects.filter(product=product, value__gt=2)
        data = ReviewSerializer(rate, many=True).data
        return data


class ProductTagSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_tags(self, product):
        return TagSerializer(product.tags.filter(is_active=True), many=True).data


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'tags', 'price', 'category', 'description']


class ProductCreateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=10)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(default=0)
    category = serializers.BooleanField()
    tags = serializers.ListField(child=serializers.IntegerField())

class TagCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_active = serializers.BooleanField()

    def validate_name(self, name):
        tags = Tag.objects.filter(name = name)
        if tags:
            raise ValidationError("Tag already existed")
        return name