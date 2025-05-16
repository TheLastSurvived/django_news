from django.contrib import admin
from django.urls import path, include  
from news import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("", views.index, name='home'),
    
    path("about/", views.about, name='about'),
    path("admin/", admin.site.urls, name='admin'),
    path("news/", include("news.urls")), 
    path('login/', views.login, name='login'),
    path("regestration/", views.regestration, name='regestration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]