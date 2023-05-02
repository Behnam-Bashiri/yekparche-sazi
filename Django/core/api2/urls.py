from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'account',AccountList )
router.register(r'base_device',Base_deviceList )
router.register(r'Cpu',CpuList )
router.register(r'Phone',PhoneList )
router.register(r'Tablet',TabletList )
router.register(r'Laptop',LaptopList )

urlpatterns = [
    path('', include(router.urls)),
]