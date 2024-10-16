from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import*
import json
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    products = Product.objects.all
    context = {'products': products}
    return render(request, 'app/home.html',context)
def adminhome(request):
    context = {}
    return render(request, 'app/adminhome.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'app/cart.html', context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('added',safe = False)
def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)
def upload(request):
    context = {}
    return render(request, 'app/upload.html', context)
def login(request):
    context = {}
    return render(request, 'app/login.html', context)
def registration(request):
    context = {}
    return render(request, 'app/registration.html', context)
def history(request):
    context = {}
    return render(request, 'app/history.html', context)
def watch(request):
    id = request.GET.get('id', '')  # Lấy id từ URL
    try:
        product = Product.objects.get(id=id)  # Lấy sản phẩm duy nhất theo id
    except Product.DoesNotExist:
        # Xử lý trường hợp sản phẩm không tồn tại
        product = None
    context = {'product': product}  # Chuyển đổi sang biến đơn lẻ
    return render(request, 'app/watch.html', context)
