from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
# from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

from bag.contexts import bag_contents

import stripe
import json

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                        "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JimkbJBRuP8yXrnGPq5EkY9Y3Jyb1cy6DDO4R91gbzkRMlsdQz6OWRz6becX3PigydoWXaFAww46bq7uJ7suTlD00tWtV1rqS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
