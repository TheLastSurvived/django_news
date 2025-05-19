from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthForm, CommentForm
from django.contrib.auth import get_user_model
from .models import News, Comment, Category
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.shortcuts import render
from django.db import models
from django.contrib.auth.decorators import login_required

User = get_user_model()
 
def index(request):
    last_three_news = News.objects.all().order_by('-pub_date')[:3]
    three_days_ago = timezone.now() - timedelta(days=3)
    

    most_commented = News.objects.filter(
        comment__created_at__gte=three_days_ago 
    ).annotate(
        num_comments=Count('comment') 
    ).order_by(
        '-num_comments'  
    ).first() 


    one_week_ago = timezone.now() - timedelta(days=7)
    
    
    top_news = News.objects.filter(
        comment__created_at__gte=one_week_ago 
    ).annotate(
        comment_count=Count('comment') 
    ).order_by(
        '-comment_count'  
    )[:5]  

    return render(request, "index.html", {'news_list': last_three_news,'most_commented': most_commented, 'top_news' : top_news })


def news(request, category_id=None):
    all_news = News.objects.all().order_by('-pub_date')

    categories = Category.objects.annotate(
        news_count=models.Count('news')
    )

    if category_id:
        all_news = News.objects.filter(category_id=category_id)
    else:
        all_news = News.objects.all()

    return render(request, "news.html",{'all_news': all_news, 'categories': categories, 'current_category_id': category_id})


def search_news(request):
    query = request.GET.get('q', '').lower()  
    results = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'search_results.html', {'results': results, 'query': query})

@login_required
def article(request, post_id):
    some_news = get_object_or_404(News, id=post_id)
    comments = Comment.objects.filter(news=post_id).order_by('-created_at')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.news = some_news
            comment.author = request.user
            comment.save()
            messages.success(request, 'Комментарий успешно добавлен!')
            return redirect('news_detail', post_id=post_id)
    else:
        form = CommentForm()
    
    return render(request, "article.html", {
        'some_news': some_news,
        'comments': comments,
        'form': form
    })


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