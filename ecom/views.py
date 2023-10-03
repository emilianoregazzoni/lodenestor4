from django.shortcuts import render
from store.models import Product
def home(request):
    products = Product.objects.all().filter(is_available=True)

#lo guardo en un dic

    context = {
        'products' : products,
    }

    return render(request,'home.html', context)