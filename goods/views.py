from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        'title': 'Home - каталог',
        'goods': goods
    }
    return render(request, template_name='goods/catalog.html', context=context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, template_name='goods/product.html', context=context)
