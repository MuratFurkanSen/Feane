from django.shortcuts import render

from order.models import *


def cart(request):
    page = 'Cart'
    user = request.user
    curr_cart = Cart.objects.filter(user=user.id)
    items = CartItem.objects.filter(cart=curr_cart)
    context = {'page': page,
               'items': items}
    return render(request, 'cart.html', context)
