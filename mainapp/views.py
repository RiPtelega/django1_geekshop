from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import BasketSlot


# links_menu = [
#     {'href': "main", 'name': 'Главная'},
#     {'href': "products", 'name': 'Продукты'},
#     {'href': "contacts", 'name': 'Контакты'},
# ]

def main(request):
    context = {'title': 'Главная'}
    return render(request, 'mainapp/main.html', context)


def products(request, pk=None):
    products = Product.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()

    context = {'title': 'Продукты', 'hot_product': Product.objects.filter(is_hot=True).first(),
               'categories': ProductCategory.objects.all(),
               'basket': basket}
    if pk is None:
        return render(request, 'mainapp/hot_product.html', context)

    if pk > 0:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = products.filter(category=category)

    context = {'title': 'Продукты', 'products': products,
               'categories': ProductCategory.objects.all(),
               'basket': basket}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {'title': 'Контакты', 'phones': ['8888888888', '999999999']}
    return render(request, 'mainapp/contacts.html', context)
