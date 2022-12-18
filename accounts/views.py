from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from Jobs.models import *
from wallets.models import *


# Create your views here.
def index(request):
    template_name = 'afripal/index.html'
    return render (request, template_name)



def register(request):
    form = UserForm()
    template_name = 'afripal/signup.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserForm()
    return render( request, template_name, context)



def login(request):
    template_name = 'afripal/signin.html'
    if request.user.is_authenticated:
        return redirect ('client-page')
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user = request.user
            if user.is_afmin == False:
                return redirect('client-page')
            else:
                return redirect('admin-page')
        else:
             messages.error(request, 'Wrong Password or username')
    return render(request, template_name)



@login_required(login_url='login')
def client_page(request):
    template_name = 'afripal/clients.html'
    return render (request, template_name)


@login_required(login_url='login')
def admin_page(request):
    pending_jobs = Job.objects.filter(state='pending')
    new_jobs = Job.objects.filter(state='pending')
    prev_jobs = Job.objects.filter(state='completed')
    incomplete_payment = Job.objects.filter(payment='pending')

    cash_list = []
    pend_list = []

    cash = Transaction.objects.all()
    for i in cash:
        if i.amount in cash_list:
            pass 
        else:
            cash_list.append(i.amount)


    for x in incomplete_payment:
        if x.budget in pend_list:
            pass 
        else:
            pend_list.append(x.budget)
   
    total = sum(cash_list)
    total_pend = sum(pend_list)

    context = {
        'pending_jobs':pending_jobs,
        'new_jobs': new_jobs,
        'prev_jobs': prev_jobs,
        'total': total,
        'total_pend':total_pend,
    }
    template_name = 'afripal/new_admin.html'
    return render (request, template_name, context)


@login_required(login_url='login')
def logout(request):
    template_name = 'afripal/index.html'
    auth.logout(request)
    return render(request, template_name)



