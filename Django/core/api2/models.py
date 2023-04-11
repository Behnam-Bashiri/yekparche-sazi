from django.db import models

# Create your models here.


class Account(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30, null=True, blank=True)
    Phone = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return 'Name : {} - Email : {}'.format(self.Name, self.Email)


class Base_device(models.Model):
    Model_device = models.CharField(max_length=20, null=True, blank=True)
    Brand = models.CharField(max_length=20, null=True, blank=True)
    ScreenSize = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return 'Model : {} - Brand : {}'.format(self.Model_device,
                                                self.Brand)


class Cpu(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Core = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return 'Name : {} - Core : {}'.format(self.Name,
                                              self.Core)


class Phone(Base_device):
    Battery = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return 'Model : {} - Brand : {}'.format(self.Model_device,
                                                self.Brand)


class Tablet(Base_device):
    pass

    def __str__(self) -> str:
        return 'Model : {} - Brand : {}'.format(self.Model_device,
                                                self.Brand)


class Laptop(Base_device):
    Cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    Ram = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return 'Model : {} - Brand : {} - cpu : {}'.format(self.Model_device,
                                                           self.Brand, self.Cpu)
