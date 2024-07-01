from rest_framework import serializers
from .models import Project, Product, News, CategoryProduct, CategoryProject, ComprehensiveEquipment, \
    CategoryComplexEquipment, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = '__all__'


class CategoryProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProject
        fields = '__all__'


class ComprehensiveEquipmentSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ComprehensiveEquipment
        fields = '__all__'


class ComprehensiveEquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryComplexEquipment
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
