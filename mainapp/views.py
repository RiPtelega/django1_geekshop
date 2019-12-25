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
    basket_quantity = 0
    basket_price = 0
    if request.user:
        basket = BasketSlot.objects.filter(user=request.user)
        for slot in basket:
            basket_quantity += slot.quantity
            basket_price += slot.price
    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = products.filter(category=category)

    context = {'title': 'Продукты', 'products': products,
               'categories': ProductCategory.objects.all(),
               'basket': basket,
               'basket_quantity': basket_quantity,
               'basket_price': basket_price}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {'title': 'Контакты', 'phones': ['8888888888', '999999999']}
    return render(request, 'mainapp/contacts.html', context)
