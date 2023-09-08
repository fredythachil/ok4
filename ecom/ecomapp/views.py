from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Categories, Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='ecomapp:login')
def allproducts(request):
    p = Paginator(Product.objects.all().filter(availability=True), 3)
    page = request.GET.get('page')
    products = p.get_page(page)

    return render(request, 'product.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'password does not match')
            return redirect('register')
    return render(request, 'register.html')


def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('ecomapp:login')
    return render(request, 'login.html')


def logoutt(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='login')
def products(request):
    products = Product.objects.all().filter(availability=True)

    return render(request, 'product.html', {'products': products})


def categories(request):
    categories = Categories.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def categoriess(request, slug):
    if (Categories.objects.filter(slug=slug)):
        p = Paginator(Product.objects.all().filter(categories__slug=slug, availability=True), 3)
        page = request.GET.get('page')
        products = p.get_page(page)
        # products=Product.objects.all().filter(categories__slug=slug,availability=True)
    else:
        messages.info(request, 'no such cat')
        return redirect('cateories')

    return render(request, 'product.html', {'products': products})


def productdetail(request, cat_slug, p_slug):
    if (Categories.objects.filter(slug=cat_slug)):
        if (Product.objects.filter(slug=p_slug)):
            products = Product.objects.filter(slug=p_slug, availability=True).first
        else:
            messages.error(request, 'No Such Product')
            return redirect('cateories')
    else:
        messages.error(request, "No Such Categories")
        return redirect('cateories')

    return render(request, 'productdetail.html', {'products': products})


def index(request):
    return render(request, 'index.html')


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        results = Product.objects.filter(name__contains=search)
        return render(request, 'search.html', {'search': search, 'results': results})
    else:
        return render(request, 'search.html' )

# def test(request):
#         return render(request, 'test.html' )
