from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории')


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение продукта')
    category = models.ForeignKey(Category.name_category, on_delete=models.CASCADE)
    price =  'f'
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
