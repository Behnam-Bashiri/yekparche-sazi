from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class PStatus(models.IntegerChoices):
    BUSY = 1, _('Busy')
    IDLE = 0, _('Idle')


class TStatus(models.IntegerChoices):
    ONPROCESS = 0, _('On Process')
    FINISHED = 1, _('Finished')
    CANCEL = 2, _('Cancel')
    UNKNOWN = 3, _('Unknown')


class PaymentStatus(models.IntegerChoices):
    ONPROCESS = 0, _('On Process')
    SUCCESS = 1, _('Success')
    CANCEL = 2, _('Cancel')
    ERROR = 3, _('Error')
    UNKNOWN = 4, _('Unknown')


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)
    status = models.IntegerField(
        choices=PStatus.choices,
        default=PStatus.IDLE,
        blank=True,
        null=True
    )
    current_X = models.CharField(max_length=20)
    current_Y = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.IntegerField(
        choices=PStatus.choices,
        default=PStatus.IDLE,
        blank=True,
        null=True
    )
    current_X = models.CharField(max_length=20)
    current_Y = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Trip(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(
        Driver, on_delete=models.SET_NULL, null=True, blank=True)
    start_location_X = models.CharField(max_length=255)
    start_location_Y = models.CharField(max_length=255)
    end_location_X = models.CharField(max_length=255)
    end_location_Y = models.CharField(max_length=255)
    pickup_time = models.DateTimeField()
    status = models.IntegerField(
        choices=TStatus.choices,
        default=TStatus.UNKNOWN,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Trip #{self.id}"


class Payment(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.IntegerField(
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNKNOWN,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Payment for Trip #{self.trip.id}"


class Reviews(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Rating for Trip #{self.trip.id}"
