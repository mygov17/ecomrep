from django.shortcuts import render, get_object_or_404
from .cart import Cart
from core.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    return render(request, 'cart/cart_summary.html', {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product')
        product = get_object_or_404(Product, id= product_id)
        cart.add(product=product)
        response = JsonResponse({'Product Name': product.name})
        return response                                                                                

def cart_delete(request):

    context = {}
    return render(request, 'core/cart_delete.html', context)

def cart_update(request):
    return render(request, 'cart/cart_update.html')

