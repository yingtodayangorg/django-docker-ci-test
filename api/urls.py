from .views import *
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('health', UserViewSet, 'healthcheck')

urlpatterns = router.urls
