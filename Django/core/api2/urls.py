from django.urls import path,include
from .views import *

urlpatterns = [
    path("test/",return_helloWolrd),
]

# 127.0.0.1:8000/api2/test/