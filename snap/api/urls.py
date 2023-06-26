from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'driver', DriverList)
router.register(r'customer', CustomerList)
router.register(r'trip', TripList)
router.register(r'reviews', ReviewsList)
router.register(r'payment', PaymentList)
router.register(r'map', MapList)
# router.register(r'auth', AuthList)

urlpatterns = [
    path('', include(router.urls)),
    # Driver
    path('drivers/<int:id_driver>/trips/', DriverList.as_view({'get': 'getTripWithDriver'}), name='getTripWithDriver'),
    path('drivers/<int:id_driver>/trips/<int:id_trip>/', DriverList.as_view({'get': 'getTripWithDriverWithID'}), name='getTripWithDriverWithID'),
    path('drivers/<int:id_driver>/trips/', DriverList.as_view({'post': 'CreateTripWithDriver'}), name='CreateTripWithDriver'),
    path('drivers/<int:id_driver>/trips/<int:id_trip>/', DriverList.as_view({'post': 'EndTrip'}), name='EndTrip'),
    # Customer
    path('customers/<int:id_customers>/trips/', CustomerList.as_view({'get': 'getTripWithCustomer'}), name='getTripWithCustomer'),
    path('customers/<int:id_customers>/trips/<int:id_trip>/', CustomerList.as_view({'get': 'getTripWithCustomerWithID'}), name='getTripWithCustomerWithID'),
    path('customers/<int:id_customers>/trips/', CustomerList.as_view({'post': 'CreateTripWithCustomer'}), name='CreateTripWithCustomer'),
    path('customers/<int:id_customers>/trips/<int:id_trip>/', CustomerList.as_view({'post': 'StartTrip'}), name='StartTrip'),
]