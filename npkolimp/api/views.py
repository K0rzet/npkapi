from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Project, Product, News, CategoryProduct, CategoryProject, ComprehensiveEquipment, \
    CategoryComplexEquipment, Image
from .serializers import ProjectSerializer, ProductSerializer, NewsSerializer, CategoryProductSerializer, \
    CategoryProjectSerializer, ComprehensiveEquipmentSerializer, ComprehensiveEquipmentCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['isNew', 'category']
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['post'])
    def add_images(self, request, pk=None):
        product = self.get_object()
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(product=product, image=image)
        return Response({'status': 'images added'})


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['post'])
    def add_images(self, request, pk=None):
        project = self.get_object()
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(project=project, image=image)
        return Response({'status': 'images added'})


class ComprehensiveEquipmentViewSet(viewsets.ModelViewSet):
    queryset = ComprehensiveEquipment.objects.all()
    serializer_class = ComprehensiveEquipmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['category']

    @action(detail=True, methods=['post'])
    def add_images(self, request, pk=None):
        equipment = self.get_object()
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(equipment=equipment, image=image)
        return Response({'status': 'images added'})


class ComprehensiveEquipmentCategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryComplexEquipment.objects.all()
    serializer_class = ComprehensiveEquipmentCategorySerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name']

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer


class CategoryProjectViewSet(viewsets.ModelViewSet):
    queryset = CategoryProject.objects.all()
    serializer_class = CategoryProjectSerializer
