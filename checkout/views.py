from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
# from django.views.decorators.http import require_POST
from django.contrib import messages
# from django.conf import settings

from .forms import OrderForm
# from .models import Order, OrderLineItem

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                        "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm(form_data)
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
