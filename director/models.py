from __future__ import unicode_literals

from django.db import models

class ECU(models.Model):
    serial_number = models.CharField(max_length=64, primary_key=True)
    public_key = models.CharField(max_length=2**12, null=False)
    cryptography_method = models.CharField(default='ed25519', max_length=16,
                                           null=False)
    primary = models.BooleanField(default=False, null=False)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE,
                                related_name='ecus')

# TODO: Records of vehicle version manifests.
# TODO: Records of director metadata sent to vehicle.
class Vehicle(models.Model):
    # TODO: Validate VIN number, but this is so low-priority.
    VIN = models.CharField(max_length=17, primary_key=True)
