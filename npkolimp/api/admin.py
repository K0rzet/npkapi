from django.contrib import admin

from .models import Product, CategoryProduct, CategoryProject, Project, News, ComprehensiveEquipment, \
    CategoryComplexEquipment, Image, ContactFormSubmission


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

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
admin.site.register(ContactFormSubmission)
