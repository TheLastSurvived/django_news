from django.urls import path
from . import views  

urlpatterns = [
    path("", views.news, name='news'),
    path("<int:post_id>/", views.article, name="news_detail"),
]