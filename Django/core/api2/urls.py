from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'account', )
router.register(r'base_device', )
router.register(r'Cpu', )
router.register(r'Phone', )
router.register(r'Tablet', )
router.register(r'Laptop', )

urlpatterns = [
    path('', include(router.urls)),
]