from .views import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('health', UserViewSet, 'healthcheck')

urlpatterns = router.urls
