from apps.carts.models import Cart, CartItem

def cart_items_count(request):
    if request.user.is_authenticated:
        # If the user is authenticated, get the cart items and calculate the count
        cart_items = CartItem.objects.filter(cart__session_key=request.session.session_key)
        total_quantity = sum(item.quantity for item in cart_items)
    else:
        total_quantity = 0
    
    return {'cart_items_count': total_quantity}