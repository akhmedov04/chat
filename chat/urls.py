from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('main/', main),
    path('user/', include('userapp.urls')),
]
