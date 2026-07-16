from django.shortcuts import render, redirect, get_object_or_404

from catalog.models import Product, Category


def index(requests):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(requests, 'catalog/index.html', context)


def matplot(requests):
    context = {
        'title': 'График'
    }
    return render(requests, 'catalog/matplot.html', context)


def contact(requests):
    context = {
        'title': 'Контакты'
    }
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        message = requests.POST.get('message')
        print(f'{name} ({email}):{message}')
    return render(requests, 'catalog/contacts.html', context)


def view_product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    context = {
        'object': product_item
    }
    return render(request, 'catalog/view_product.html', context)


def create_category(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        cat_desc = request.POST.get('cat_desc')
        Category.objects.create(name=cat_name, description=cat_desc)
        return redirect('catalog:contacts')
    return render(request, 'catalog/create_category.html')


def create_product(request):
    if request.method == 'POST':
        prod_category = request.POST.get('prod_category')
        name = request.POST.get('prod_name')
        price = request.POST.get('prod_price')
        description = request.POST.get('prod_desc')
        prod_image = request.FILES.get('prod_image')
        Product.objects.create(name=name, description=description, price=price,
                               image=prod_image, category=Category.objects.get(id=prod_category))
        print(f"Данные:\n"
              f"Название: {name}\n"
              f"Описание: {description}\n"
              f"Цена: {price}\n"
              f"Фото: {prod_image}\n"
              f"Категория: {prod_category}")
    return render(request, 'catalog/create_product.html', {'categories': Category.objects.all()})
