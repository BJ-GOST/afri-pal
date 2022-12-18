import stripe 
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000/payment'



@login_required(login_url='login')
@csrf_exempt
def create_checkout_session(request):
    data = json.load(request)
    name = data['name']
    amount= data['amount']
    id = data['Id']
    job = Job.objects.get(id=id)
    job.payment = 'completed'
    job.save()
    
    Client = job.customer

    #creating and saving the transaction to the database
    transaction = Transaction(client=Client, job=job, amount=amount)
    transaction.save()



    print (f'[name: {name}; amount: {amount}; id: {id}]')
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
    'price_data': {
    'currency': 'usd',
    'product_data': {
    'name': name,
    },
    'unit_amount': amount,
    },
    'quantity': 1,
    }],
    mode='payment',
    success_url=YOUR_DOMAIN + '/success.html',
    cancel_url=YOUR_DOMAIN + '/cancel.html',
    )
    return JsonResponse({'id': session.id})



@login_required(login_url='login')
def home(request):
    return render(request,'checkout.html')


@login_required(login_url='login')
def success(request):
    return render(request,'success.html')


@login_required(login_url='login')
def cancel(request):
    return render(request,'afripal\clients.html')


