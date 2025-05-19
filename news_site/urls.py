from django.contrib import admin
from django.urls import path, include  
from news import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
    
    path("about/", views.about, name='about'),
    path("admin/", admin.site.urls, name='admin'),
    path("news/", include("news.urls")), 
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', views.search_news, name='search_news'),
    path('api/', include('api.urls')),  
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)