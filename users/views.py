from django.shortcuts import render,get_object_or_404, redirect
from accounts.models import User
from products.models import Products
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model



# profile
def profile(request, pk):
    user = User.objects.get(pk=pk)
    UserProducts = user.products_user.all()
    context = {'user': user, 'UserProducts': UserProducts}
    return render(request, 'users/profile.html', context)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect('index')
    return redirect('accounts:login')


def follow(request, pk):
    if request.user.is_authenticated:
        menber = get_object_or_404(get_user_model(), pk=pk)
        if menber != request.user:
            if menber.follwers.filter(pk=request.user.pk).exists():
                menber.follwers.remove(request.user)
            else:
                menber.follwers.add(request.user)
        return redirect('users:profile', menber.pk)
    return redirect('account:login')