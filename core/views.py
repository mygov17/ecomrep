from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
# views.py


def search_products(request):
    query = request.GET.get('q')  # 'q' is the name of the search input field
    products = Product.objects.filter(name__icontains=query) if query else []
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'core/search.html', context)


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'core/category_summary.html',{'categories':categories})


def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name__iexact=foo)  # Case-insensitive match 
        products = Product.objects.filter(category=category)
        return render(request, 'core/category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.error(request, "That Category Doesn't Exist.")

        return redirect('home')

# def category(request, foo):
# 	# Replace Hyphens with Spaces
# 	foo = foo.replace('-', ' ')
# 	# Grab the category from the url
# 	try:
# 		# Look Up The Category
# 		category = Category.objects.get(name=foo)
# 		products = Product.objects.filter(category=category)
# 		return render(request, 'core/category.html', {'products':products, 'category':category})
# 	except:
# 		messages.success(request, ("That Category Doesn't Exist..."))
# 		return redirect('home')

def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products':products})

@login_required
def about(request):
    return render(request, 'core/about.html')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'core/product.html', {'product':product})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user)
            messages.success(request, f"You are logged in as {username}")
            return redirect('home')
        else:
            messages.success(request, ('Username or password is not correct.. please try again'))
    return render(request, 'core/login.html')

def logoutPage(request):
    logout (request)
    messages.success(request, f"You have logged out")
    return redirect('login')


def registerPage(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login (request, user)
            messages.success(request, f"You have registered {username}")
            return redirect('login')
        else:
            messages.success(request, f"please check our chiterials to sign up")
            return redirect('register')
    else:
        return render(request, 'core/register.html', {'form':form})
    
