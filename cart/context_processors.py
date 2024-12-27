from .cart import Cart
#Create context processor for all pages
def cart(request):
    return {'cart':Cart(request)}