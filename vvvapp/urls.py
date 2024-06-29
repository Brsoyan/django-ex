from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddUserRequestViewSet, PingRequestViewSet

router = DefaultRouter()
router.register(r'addUser', AddUserRequestViewSet)
router.register(r'ping', PingRequestViewSet)


urlpatterns = [
    path('', include(router.urls)),
]