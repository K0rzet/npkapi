from django.core.exceptions import ValidationError
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Image(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey('Project', related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    equipment = models.ForeignKey('ComprehensiveEquipment', related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.product or self.project or self.equipment}"

    def clean(self):
        if sum(bool(x) for x in [self.product, self.project, self.equipment]) > 1:
            raise ValidationError('Image can be related to only one type of object.')


class CategoryProduct(models.Model):
    image = models.ImageField(upload_to='categories/images/')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryProject(models.Model):
    image = models.ImageField(upload_to='categories/images/')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryComplexEquipment(models.Model):
    image = models.ImageField(upload_to='categories/images/')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(CategoryProduct, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isNew = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(CategoryProject, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class ComprehensiveEquipment(models.Model):
    category = models.ForeignKey(CategoryComplexEquipment, related_name='comprehensive_equipments', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='news/images/')
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    isCompleted = models.BooleanField(default = False, blank = True, null = True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
