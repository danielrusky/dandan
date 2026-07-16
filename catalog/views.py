from django.shortcuts import render

from catalog.models import Product


def index(requests):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(requests, 'catalog/index.html', context)


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
