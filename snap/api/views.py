from rest_framework import viewsets, status
from rest_framework import status
from rest_framework.serializers import Serializer
from .serilizers import *
from rest_framework import filters
from .models import *
from .serilizers import *
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissions
from datetime import datetime, date
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

CustomUser = get_user_model()


class TemplateViewSet(viewsets.ModelViewSet):
    ordering_fields = '__all_related__'
    queryset = ''
    serializer_class = ''

    def list(self, request):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return JsonResponse({'message': 'این عمل قابل انجام نیست'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class DriverList(TemplateViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializers

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        try:
            # Assuming the ID is passed as a query parameter
            driver_id = request.query_params.get('driver_id')
            if driver_id is not None:
                try:
                    queryset = self.get_queryset().filter(id=driver_id)
                    if not queryset.exists():
                        return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': 1, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in retrieving data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': count, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return JsonResponse({'message': 'Data created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'message': 'Problem in creating data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse({'message': 'Update successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message': 'Update failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.delete()
            return JsonResponse({'message': 'Delete successful'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'message': 'Delete failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getTripWithDriver(self, request, id_driver):
        try:
            driver = Driver.objects.get(id=id_driver)
            trips = Trip.objects.filter(driver=driver)
            response_data = {
                'driver': {
                    'id': driver.id,
                    'name': driver.user.username,
                    'car_model': driver.car_model,
                    'license_plate': driver.license_plate,
                    'status': driver.status,
                    'current_X': driver.current_X,
                    'current_Y': driver.current_Y,
                },
                'trips': [
                    {
                        'id': trip.id,
                        'date': trip.date,
                        'time': trip.time,
                        'customer_id': trip.customer_id,
                        'driver_id': trip.driver_id,
                        'start_location_X': trip.start_location_X,
                        'start_location_Y': trip.start_location_Y,
                        'end_location_X': trip.end_location_X,
                        'end_location_Y': trip.end_location_Y,
                        'pickup_time': trip.pickup_time,
                        'status': trip.status,
                    }
                    for trip in trips
                ]
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        except Driver.DoesNotExist:
            return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getTripWithDriverWithID(self, request, id_driver, id_trip):
        try:
            driver = Driver.objects.get(id=id_driver)
            trip = Trip.objects.get(id=id_trip, driver=driver)
            response_data = {
                'driver': {
                    'id': driver.id,
                    'name': driver.user.username,
                    'car_model': driver.car_model,
                    'license_plate': driver.license_plate,
                    'status': driver.status,
                    'current_X': driver.current_X,
                    'current_Y': driver.current_Y,
                },
                'trip': {
                    'id': trip.id,
                    'date': trip.date,
                    'time': trip.time,
                    'customer_id': trip.customer_id,
                    'driver_id': trip.driver_id,
                    'start_location_X': trip.start_location_X,
                    'start_location_Y': trip.start_location_Y,
                    'end_location_X': trip.end_location_X,
                    'end_location_Y': trip.end_location_Y,
                    'pickup_time': trip.pickup_time,
                    'status': trip.status,
                }
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        except Driver.DoesNotExist:
            return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
        except Trip.DoesNotExist:
            return JsonResponse({'message': 'Trip not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def CreateTripWithDriver(self, request, id_driver):
        try:
            driver = Driver.objects.get(id=id_driver)
            trip = Trip.objects.create(driver=driver, **request.data)
            response_data = {
                'driver': {
                    'id': driver.id,
                    'name': driver.user.username,
                    'car_model': driver.car_model,
                    'license_plate': driver.license_plate,
                    'status': driver.status,
                    'current_X': driver.current_X,
                    'current_Y': driver.current_Y,
                },
                'trip': {
                    'id': trip.id,
                    'date': trip.date,
                    'time': trip.time,
                    'customer_id': trip.customer_id,
                    'driver_id': trip.driver_id,
                    'start_location_X': trip.start_location_X,
                    'start_location_Y': trip.start_location_Y,
                    'end_location_X': trip.end_location_X,
                    'end_location_Y': trip.end_location_Y,
                    'pickup_time': trip.pickup_time,
                    'status': trip.status,
                }
            }
            return JsonResponse(response_data, status=status.HTTP_201_CREATED)
        except Driver.DoesNotExist:
            return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def EndTrip(self, request, id_trip, id_driver):
        try:
            driver = Driver.objects.get(id=id_driver)
            trip = Trip.objects.create(driver=driver, **request.data)
            response_data = {
                'driver': {
                    'id': driver.id,
                    'name': driver.user.username,
                    'car_model': driver.car_model,
                    'license_plate': driver.license_plate,
                    'status': driver.status,
                    'current_X': driver.current_X,
                    'current_Y': driver.current_Y,
                },
                'trip': {
                    'id': trip.id,
                    'date': trip.date,
                    'time': trip.time,
                    'customer_id': trip.customer_id,
                    'driver_id': trip.driver_id,
                    'start_location_X': trip.start_location_X,
                    'start_location_Y': trip.start_location_Y,
                    'end_location_X': trip.end_location_X,
                    'end_location_Y': trip.end_location_Y,
                    'pickup_time': trip.pickup_time,
                    'status': trip.status,
                }
            }
            return JsonResponse(response_data, status=status.HTTP_201_CREATED)
        except Driver.DoesNotExist:
            return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'],detail=False)
    def search(self, request):
        try:
            X = request.query_params.get('X')
            Y = request.query_params.get('Y')
            try:
                driver_obj = Driver.object.get(current_X=X,current_Y=Y)
                serializer = self.get_serializer(driver_obj, many=True)
                return JsonResponse({'count': 1, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
            except Driver.DoesNotExist:
                return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
class CustomerList(TemplateViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        try:
            # Assuming the ID is passed as a query parameter
            customer_id = request.query_params.get('customer_id')
            if customer_id is not None:
                try:
                    queryset = self.get_queryset().filter(id=customer_id)
                    if not queryset.exists():
                        return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': 1, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in retrieving data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': count, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return JsonResponse({'message': 'Data created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'message': 'Problem in creating data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse({'message': 'Update successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message': 'Update failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.delete()
            return JsonResponse({'message': 'Delete successful'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'message': 'Delete failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getTripWithCustomer(self, request, id_customers):
        try:
            customer = Customer.objects.get(id=id_customers)
            trips = Trip.objects.filter(driver=customer)
            response_data = {
                'customer': {
                    'id': customer.id,
                    'name': customer.user.username,
                    'phone_number': customer.phone_number,
                    'address': customer.address,
                    'status': customer.status,
                    'current_X': customer.current_X,
                    'current_Y': customer.current_Y,
                },
                'trips': [
                    {
                        'id': trip.id,
                        'date': trip.date,
                        'time': trip.time,
                        'customer_id': trip.customer_id,
                        'driver_id': trip.driver_id,
                        'start_location_X': trip.start_location_X,
                        'start_location_Y': trip.start_location_Y,
                        'end_location_X': trip.end_location_X,
                        'end_location_Y': trip.end_location_Y,
                        'pickup_time': trip.pickup_time,
                        'status': trip.status,
                    }
                    for trip in trips
                ]
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getTripWithCustomerWithID(self, request, id_customers, id_trip):
        try:
            customer = Customer.objects.get(id=id_customers)
            trip = Trip.objects.get(id=id_trip, customer=customer)
            response_data = {
                'customer': {
                    'id': customer.id,
                    'name': customer.user.username,
                    'phone_number': customer.phone_number,
                    'address': customer.address,
                    'status': customer.status,
                    'current_X': customer.current_X,
                    'current_Y': customer.current_Y,
                },
                'trips': [
                    {
                        'id': trip.id,
                        'date': trip.date,
                        'time': trip.time,
                        'customer_id': trip.customer_id,
                        'driver_id': trip.driver_id,
                        'start_location_X': trip.start_location_X,
                        'start_location_Y': trip.start_location_Y,
                        'end_location_X': trip.end_location_X,
                        'end_location_Y': trip.end_location_Y,
                        'pickup_time': trip.pickup_time,
                        'status': trip.status,
                    }
                ]
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def CreateTripWithCustomer(self, request, id_customers):
        try:
            customer = Customer.objects.get(id=id_customers)
            trip = Trip.objects.create(customer=customer, **request.data)
            response_data = {
                'customer': {
                    'id': customer.id,
                    'name': customer.user.username,
                    'phone_number': customer.phone_number,
                    'address': customer.address,
                    'status': customer.status,
                    'current_X': customer.current_X,
                    'current_Y': customer.current_Y,
                },
                'trips': [
                    {
                        'id': trip.id,
                        'date': trip.date,
                        'time': trip.time,
                        'customer_id': trip.customer_id,
                        'driver_id': trip.driver_id,
                        'start_location_X': trip.start_location_X,
                        'start_location_Y': trip.start_location_Y,
                        'end_location_X': trip.end_location_X,
                        'end_location_Y': trip.end_location_Y,
                        'pickup_time': trip.pickup_time,
                        'status': trip.status,
                    }
                ]
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def StartTrip(self, request, id_trip, id_driver):
        try:
            customer = Customer.objects.get(id=id_driver)
            trip = Trip.objects.create(customer=customer, **request.data)
            response_data = {
                'customer': {
                    'id': customer.id,
                    'name': customer.user.username,
                    'phone_number': customer.phone_number,
                    'address': customer.address,
                    'status': customer.status,
                    'current_X': customer.current_X,
                    'current_Y': customer.current_Y,
                },
                'trips': [
                    {
                        'id': trip.id,
                        'date': trip.date,
                        'time': trip.time,
                        'customer_id': trip.customer_id,
                        'driver_id': trip.driver_id,
                        'start_location_X': trip.start_location_X,
                        'start_location_Y': trip.start_location_Y,
                        'end_location_X': trip.end_location_X,
                        'end_location_Y': trip.end_location_Y,
                        'pickup_time': trip.pickup_time,
                        'status': trip.status,
                    }
                ]
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': 'Error - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)


class TripList(TemplateViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializers

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        try:
            # Assuming the ID is passed as a query parameter
            trip_id = request.query_params.get('trip_id')
            if trip_id is not None:
                try:
                    queryset = self.get_queryset().filter(id=trip_id)
                    if not queryset.exists():
                        return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': 1, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in retrieving data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': count, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return JsonResponse({'message': 'Data created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'message': 'Problem in creating data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse({'message': 'Update successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message': 'Update failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.delete()
            return JsonResponse({'message': 'Delete successful'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'message': 'Delete failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)


class ReviewsList(TemplateViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        try:
            # Assuming the ID is passed as a query parameter
            review_id = request.query_params.get('review_id')
            if review_id is not None:
                try:
                    queryset = self.get_queryset().filter(id=review_id)
                    if not queryset.exists():
                        return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': 1, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in retrieving data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': count, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return JsonResponse({'message': 'Data created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'message': 'Problem in creating data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse({'message': 'Update successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'message': 'Update failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.delete()
            return JsonResponse({'message': 'Delete successful'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'message': 'Delete failed - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentList(TemplateViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        try:
            # Assuming the ID is passed as a query parameter
            payment_id = request.query_params.get('payment_id')
            if payment_id is not None:
                try:
                    queryset = self.get_queryset().filter(id=payment_id)
                    if not queryset.exists():
                        return JsonResponse({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': 1, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in retrieving data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    serializer = self.get_serializer(queryset, many=True)
                    return JsonResponse({'count': count, 'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
                except Exception as e:
                    return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'message': 'Problem in Retrieving Data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return JsonResponse({'message': 'Data created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'message': 'Problem in creating data - {}'.format(e)}, status=status.HTTP_400_BAD_REQUEST)

# class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = serializers.CustomUserRetrieveSerializer
#     permission_classes = (permissions.IsAuthenticated,)


#     def get_object(self):
#         return self.request.user
