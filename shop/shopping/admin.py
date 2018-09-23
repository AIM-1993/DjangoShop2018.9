from django.contrib import admin
from .models import Product, Category
# Register your models here.

# 商品列表
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', '名称', '图片']

admin.site.register(Category, CategoryAdmin)

# Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', '名称', '图片', '所属类别', '价格', '库存', '上架情况', '创建时间', '修改时间']
    list_editable = ['名称', '所属类别', '价格', '库存', '上架情况']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
