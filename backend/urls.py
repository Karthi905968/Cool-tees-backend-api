from django.contrib import admin
from django.urls import path,include
from subapp import urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('post/',include(urls))
]
