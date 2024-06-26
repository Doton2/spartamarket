from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_POST,require_http_methods


# from .forms import CustomUserCreationForm


# Create your views here.

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_path= request.GET.get('next') or 'index'
            return redirect(next_path)
    else: 
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('index')


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request,'accounts/signup.html', context)





