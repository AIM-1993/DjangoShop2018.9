from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def home(request):
    所有类别 = Category.objects.all()
    Data = []
    for cate in 所有类别:
        Data.append((cate, Product.objects.filter(所属类别=cate)[:3]))
    content = {'Data': Data}
    return render(request, 'shopping/home.html', content)
