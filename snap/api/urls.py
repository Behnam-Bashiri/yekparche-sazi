from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'driver', DriverList)
router.register(r'customer', CustomerLisr)
router.register(r'trip', TripList)
router.register(r'auth', AuthList)
router.register(r'reviews', ReviewsList)
router.register(r'payment', PaymentList)

urlpatterns = [
    path('', include(router.urls)),
]