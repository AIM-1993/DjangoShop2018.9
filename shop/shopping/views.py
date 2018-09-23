from django.shortcuts import render
from .models import 产品列表, 商品类别表
# Create your views here.


def home(request):
    content = {'所有商品': 产品列表.objects.all()}
    return render(request, 'shopping/home.html', content)
