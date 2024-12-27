class Cart():
    def __int__(self, request):
        self.session = request.session
        #Get the current session key if it exit
        cart = self.session.get('session_key')
        #if the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key']= {}
            
            #make sure cart is availabe on all pages of site
            self.cart = cart

    def add(self, product):
        product_id = str(product_id)
        if product_id in self.cart:
            pass
        else:
            self.cart['product_id']= {'price':str(product.price)}
        self.session.modify = True 