from django.shortcuts import render

links_menu = [
    {'href': "main", 'name': 'Главная'},
    {'href': "products", 'name': 'Продукты'},
    {'href': "contacts", 'name': 'Контакты'},
]

def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная', 'links_menu': links_menu})


def products(request):
    context = {'title': 'Продукты', 'products': ['Винни-Пух', 'Потапыч'], 'links_menu': links_menu}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {'title': 'Контакты', 'phones': ['8888888888', '999999999'], 'links_menu': links_menu}
    return render(request, 'mainapp/contacts.html', context)
