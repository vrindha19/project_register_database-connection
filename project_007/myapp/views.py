from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
def index(request):
    # Your logic for the index view goes here
    return render(request, 'index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, ForgotPasswordForm, SignupForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                # Redirect to a success page
                return redirect('products')  # Change 'success_page' to your success page URL
            else:
                # Invalid login credentials, handle accordingly
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Process the form data, send email, etc.
            pass
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            # Redirect to the login page after successful signup
            return redirect('login')  # Change 'login' to your login page URL
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})


def product_view(request):
    # Your logic for the product view goes here
    return render(request, 'view_product.html')

# def members(request):
#     return render(request,'index2.html')
def home(request):
    return render(request,'index.html')
def fruits(request):
    return render(request,'fruits.product.html')
def vegitables(request):
    return render(request,'vegitables.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def payment(request):
    return render(request,'view_payment.html')
def contact(request):
    return render(request,'contact.html')
def add_product(request):
    return render(request,'add_product.html')
def shopping_cart(request):
    return render(request,'shopping_cart.html')
def view_product(request):
    return render(request,'view_product.html')
def forgot_password(request):
    return render(request,'forgot_password.html')
def about(request):
    return render(request,'about.html')
def view_order(request):
    return render(request,'view_orders.html')
def orderpage(request):
    return render(request,'orderpage.html')
def add_product(request):
    return render(request,'add_product.html')
def logout(request):
    return render(request,'logout.html')
def logout_action(request):
    return render(request,'logout-action.html')
def orderpage(request):
    return render(request,'orderpage.html')