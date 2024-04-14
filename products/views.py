from django.shortcuts import render, redirect
from .forms import FormProducts
from .models import Products
from django.contrib.auth.decorators import login_required

# Create your views here.
def product(request,pk):
    products = Products.objects.get(pk=pk)
    context = {'products': products}
    return render(request, 'products/products.html',context )


@login_required
def create(request):
    if request.method == 'POST':
        form = FormProducts(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('index')
    else:
            form = FormProducts()
    context = { "form":form}
    return render(request, 'products/create.html',context )


def update(request, pk):
    product = Products.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormProducts(request.POST, request.FILES,instance=product )
        if form.is_valid():
            form.save()
            return redirect('products:product',pk)
    else:
        form = FormProducts(instance=product)
    context = {'form':form, 'product':product}
    return render(request, 'products/update.html', context)


def delete(request, pk):
    deletes = Products.objects.get(pk=pk)
    Products.delete(deletes)
    return redirect('index')
