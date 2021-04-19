from django.contrib import admin

from .models import DonationRequest, VolunteerSlot

admin.site.register(DonationRequest)
admin.site.register(VolunteerSlot)