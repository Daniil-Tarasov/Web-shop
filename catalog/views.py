from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product, Contacts


def home(request):
    latest_products = Product.objects.order_by('created_at')[:5]
    products = Product.objects.all()

    for product in latest_products:
        print(
            f'{product.name_product}: {product.description}. Дата создания: {product.created_at}. Цена: {product.price}')

    return render(request, 'home.html', {'products': products})


def contacts(request):
    contacts_list = Contacts.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Мы обязательно с вами свяжемся.")
    return render(request, 'contacts.html', {'contacts': contacts_list})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        'product_name': product.name_product,
        'description': product.description,
        'image': product.image,
        'category': product.category,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at
    }
    return render(request, 'product_detail.html', context=context)
