from django.contrib import admin
from .models import ShopUser
from basketapp.models import BasketSlot

# Register your models here.

admin.site.register(ShopUser)


class BasketInLine(admin.TabularInline):
    model = BasketSlot
    extra = 0


class ShopUserWithBasket(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True


@admin.register(ShopUserWithBasket)
class ShopUserWithBasketAdmin(admin.ModelAdmin):
    list_display = 'username', 'get_basket_quantity', 'get_basket_cost',
    fields = 'username',
    readonly_fields = 'username',
    inlines = BasketInLine,

    def get_queryset(self, request):
        return ShopUser.objects.filter(basket__quantity__gt=0).distinct()

    def get_basket_quantity(self, instance):
        return sum(list(map(
            lambda basket_slot: basket_slot.quantity, instance.basket.all())))

    def get_basket_cost(self, instance):
        return sum(list(map(
            lambda basket_slot: basket_slot.price, instance.basket.all())))

    get_basket_quantity.short_description = 'Товаров в корзине'
    get_basket_cost.short_description = 'Стоимость корзины'




