from django.contrib import admin
from django.urls import path, include
from . import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.router.urls)),
]

