from django.shortcuts import render
from home1.models import *
# Create your views here.

def index(request):
    cateParents = Category.objects.filter(cate_parent_id = 0)
    featureItems = Product.objects.filter(product_status = True)
    context = {
        'parents': cateParents,
        'featureItems': featureItems,
    }
    return render(request, "home/index.html", context)