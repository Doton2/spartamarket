from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request,'accounts/signup.html', context)