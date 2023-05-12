from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginview),
    path('register/', registerview),
    # path('home/', home),
    path('logout/', logoutview),
]