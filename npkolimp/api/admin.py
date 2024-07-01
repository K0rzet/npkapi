from django.contrib import admin

from .models import Product, CategoryProduct, CategoryProject, Project, News, ComprehensiveEquipment, \
    CategoryComplexEquipment, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

    def get_queryset(self, request):
        # Get the parent object (product, project, or equipment)
        parent_obj = self.parent_model.objects.get(pk=self.parent_obj_id)
        # Filter images based on the parent object
        return super().get_queryset(request).filter(
            product=parent_obj if isinstance(parent_obj, Product) else None,
            project=parent_obj if isinstance(parent_obj, Project) else None,
            equipment=parent_obj if isinstance(parent_obj, ComprehensiveEquipment) else None
        )

    def get_formset(self, request, obj=None, **kwargs):
        # Save the parent object's ID for use in get_queryset
        self.parent_obj_id = obj.id if obj else None
        return super().get_formset(request, obj, **kwargs)

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['id', 'title', 'category', 'price', 'isNew']
    search_fields = ['title', 'description']
    list_filter = ['isNew', 'category']

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'category']
    search_fields = ['title', 'description']
    list_filter = ['category']

class ComprehensiveEquipmentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'category']
    search_fields = ['title', 'description']
    list_filter = ['category']

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class CategoryProjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class CategoryComplexEquipmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(CategoryProject, CategoryProjectAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(News)
admin.site.register(ComprehensiveEquipment, ComprehensiveEquipmentAdmin)
admin.site.register(CategoryComplexEquipment, CategoryComplexEquipmentAdmin)