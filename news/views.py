from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthForm
from django.contrib.auth import get_user_model

User = get_user_model()
 
def index(request):
    return render(request, "index.html")


def news(request):
    return render(request, "news.html")


def article(request, post_id):
    return render(request, "article.html")


def about(request):
    return render(request, "about.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('news')
    
    if request.method == 'POST':
        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = CustomAuthForm()
    
    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация прошла успешно! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "registration.html", {'form': form})