from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main import models


def dashboard(request):
    categorys = models.Category.objects.all()
    products = models.Product.objects.all()
    users = User.objects.all()
    context = {
        'categorys':categorys,
        'products':products,
        'users':users,
    }
    return render(request, 'dashboard/index.html', context)


def category_list(request):
    categorys = models.Category.objects.all()
    return render(request, 'category/list.html', {'categorys':categorys})


def category_detail(request, id):
    category = models.Category.objects.get(id=id)
    products = models.Product.objects.filter(category=category, is_active=True)
    context = {
        'category':category,
        'products':products
    }
    return render(request, 'category/list.html', context)


def category_update(request, id):
    category = models.Category.objects.get(id=id)
    category.name = request.POST['name']
    category.save()
    return redirect('category_detail', category.id)


def category_delete(request, id):
    category = models.Category.objects.get(id=id)
    category.delete()
    return redirect('category_list')




# products

def products(request):
    products = models.Product.objects.all()
    return render(request, 'dashboard/products/list.html', {'products':products})


def product_create(request):
    categorys = models.Category.objects.all()
    context = {
        'categorys':categorys
    }
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        quantity = request.POST['quantity']
        price = request.POST['price']
        currency = request.POST['currency']
        baner_image = request.FILES['baner_image']
        category_id = request.POST['category_id']
        images = request.FILES.getlist('images')
        product = models.Product.objects.create(
            name=name,
            description = description,
            quantity=quantity,
            price=price,
            currency=currency,
            baner_image=baner_image,
            category_id=category_id
        )
        for image in images:
            models.ProductImage.objects.create(
                image=image,
                product=product
            )

    return render(request, 'dashboard/products/create.html', context)


def create_enter(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        models.EnterProduct.objects.create(
            product_id=product_id,
            quantity=quantity
        )
        return redirect('dashboard:list_enter')
    return render(request, 'dashboard/enter/create.html', {'products':models.Product.objects.all()})


def update_enter(request, id):
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        enter = models.EnterProduct.objects.get(id=id)
        enter.quantity = quantity
        enter.save()
    return redirect('dashboard:list_enter')


def delete_enter(request, id):
    models.EnterProduct.objects.get(id=id).delete()
    return redirect('dashboard:list_enter')


def list_enter(request):
    enters = models.EnterProduct.objects.all()
    context = {'enters':enters}
    return render(request, 'dashboard/enter/list.html', context)