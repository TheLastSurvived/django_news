from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NewsViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'news', NewsViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]