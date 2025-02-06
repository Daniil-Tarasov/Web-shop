from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product, Contacts, Category


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


def add_product(request):

    if request.method == 'POST':
        name_product = request.POST.get('name_product')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        name_category=None
        if category:
            try:
                name_category = Category.get(name_category=category)
            except Category.DoesNotExist:
                return HttpResponse("Категория не найдена.")


        product = Product(
            name_product=name_product,
            category=name_category,
            description=description,
            price=price,
            image=image,
        )

        product.save()
        return HttpResponse(f"Товар {name_product} успешно добавлен!")
    return render(request, 'add_product_user.html')
