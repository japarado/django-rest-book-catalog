from django.urls import path, include
from rest_framework.routers import DefaultRouter

from catalog.views import LibraryViewSet, BookViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('libraries', LibraryViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
