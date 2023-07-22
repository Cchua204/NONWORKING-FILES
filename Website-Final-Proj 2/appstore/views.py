from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserLoginForm, UserRegistrationForm, AddToCartForm
from quotations.models import Quotation
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")

def usernames111(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

def my_view(request, customer_id):
    customer = get_object_or_404(Quotation, customer_id=customer_id)
    
    context = {
        'customer': customer,
    }
    return render(request, 'quotation.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout


def cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            action = form.cleaned_data['action']
            quotation = Quotation.objects.get(customer_id=request.user.id)  # Replace request.user.id with the actual customer ID
            if action == 'add':
                quotation.item_bought.append(item)
            elif action == 'remove':
                quotation.item_bought.remove(item)
            quotation.save()
            return redirect('cart')  # Redirect back to the cart page after adding/removing an item
    else:
        form = AddToCartForm()

    quotation = Quotation.objects.get(customer_id=request.user.id)  # Replace request.user.id with the actual customer ID
    context = {
        'form': form,
        'cart_items': quotation.item_bought,
    }
    return render(request, 'cart.html', context)
