from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from mainapp.models import Product
from .models import BasketSlot


@login_required
def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()
    return render(request, 'basketapp/basket.html', {'basket_items': basket})


@login_required
def add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(product=product.pk).first()
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[product_pk]))
    if basket_slot:
        basket_slot.quantity += 1
        basket_slot.save()
    else:
        BasketSlot(user=request.user, product=product).save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(product=product.pk).first()
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[product_pk]))
    if basket_slot:
        if basket_slot.quantity <= 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit(request, pk):
    if request.is_ajax():
        basket_slot = get_object_or_404(BasketSlot, pk=pk)
        quantity = int(request.GET.get('quantity'))
        if quantity > 0:
            basket_slot.quantity = quantity
            basket_slot.save()
        else:
            basket_slot.delete()
    return HttpResponse('Ok')
