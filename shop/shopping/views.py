from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def home(request):
    Cate_data = Category.objects.all()
    Cate_info = []
    for cate in Cate_data:
        Cate_info.append(Category, Product.objects.filter(cate=cate)[:3])
    content = {'Cate_info': Cate_info}
    return render(request, 'shopping/home.html', content)
