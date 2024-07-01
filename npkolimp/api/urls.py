from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProjectViewSet, NewsViewSet, CategoryProductViewSet, \
    CategoryProjectViewSet, ComprehensiveEquipmentViewSet, ComprehensiveEquipmentCategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'category-product', CategoryProductViewSet, basename='category-product')
router.register(r'category-project', CategoryProjectViewSet, basename='category-project')
router.register(r'comprehensive-equipment', ComprehensiveEquipmentViewSet, basename='comprehensive-equipment')
router.register(r'comprehensive-equipment-category', ComprehensiveEquipmentCategoryViewSet, basename='comprehensive-equipment-category')


urlpatterns = [
    path('', include(router.urls)),

]

