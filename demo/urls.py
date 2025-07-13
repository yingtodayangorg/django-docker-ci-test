from django.contrib import admin
from django.urls import path, include
from healthcheck.views import healthcheck

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('health/', healthcheck)
]
