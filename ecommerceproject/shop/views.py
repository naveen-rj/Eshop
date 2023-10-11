from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import UserRegistrationForm
from shop.models import Category, Product, CartItem


# Create your views here.
def home(request, slug_c=None):
    page_c = None
    products = None
    category_products = None
    if slug_c is not None:
        page_c = get_object_or_404(Category, slug=slug_c)
        products = Product.objects.all().filter(category=page_c, available=True)
    else:
        categories = Category.objects.all()
        category_products = {}
        for category in categories:
            products = Product.objects.filter(category=category, available=True)
            category_products[category] = products

    # products_group = [products[i: i+3] for i in range(0, len(products), 3)]
    return render(request, 'home.html',
                  {'category': page_c, 'category_products': category_products, 'products': products})


def cart(request):
    return render(request, 'cart.html')


def prod_details(request, slug_c, slug_p):
    try:
        product = Product.objects.get(category__slug=slug_c, slug=slug_p)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})


def payments(request):
    return render(request, 'payments.html')


def signup_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def signin_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Username or Password'
    else:
        error_message = None
    return render(request, 'signin.html', {'error_message': error_message})


def signout_user(request):
    logout(request)
    return redirect('home')


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def view_cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            item.subtotal = item.quantity * item.product.price
        total_amt = sum(item.subtotal for item in cart_items)
        return render(request, 'cart.html', {'cart_items': cart_items,
                                             'total_amt': total_amt})
    else:
        return render(request, 'cart.html')
