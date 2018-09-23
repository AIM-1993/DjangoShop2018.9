from django.db import models

# Create your models here.
class Category(models.Model):
    名称 = models.CharField(max_length=50, unique=True)
    描述 = models.TextField(blank=True)
    图片 = models.ImageField(upload_to='category', blank=True)
    class Meta:
        verbose_name_plural = "Category"
        db_table = "Category"

    def __str__(self):
        return self.名称


class Product(models.Model):
    名称 = models.CharField(max_length=100, unique=True)
    描述 = models.TextField(blank=True)
    图片 = models.ImageField(upload_to='category', blank=True)
    所属类别 = models.ForeignKey(Category, on_delete=models.CASCADE)
    价格 = models.DecimalField(max_digits=10, decimal_places=2)
    上架情况 = models.BooleanField(default=True)
    创建时间 = models.DateField(auto_now_add=True)
    修改时间 = models.DateField(auto_now_add=True)
    库存 = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Product"
        db_table = "Product"
        ordering = ('-创建时间',)

    def __str__(self):
        return self.名称
