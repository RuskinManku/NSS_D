from django.db import models
from django.core.validators import RegexValidator
from django.utils.timezone import now
from pytz import timezone


class VolunteerSlot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    idno = models.CharField(max_length=500)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    slot_register_time = models.DateTimeField(default=now)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)

    def __str__(self):
        s = self.slot_id
        s = 'Volunteer ' + str(s)
        return s

class DonationRequest(models.Model):
    req_id = models.AutoField(primary_key=True)
    slot = models.ForeignKey(VolunteerSlot, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    items = models.CharField(max_length=500)
    time_of_request = models.DateTimeField(default=now)

    def __str__(self):
        s = self.req_id
        s = 'Request ' + str(s)
        return s