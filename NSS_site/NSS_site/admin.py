from django.contrib import admin

from .models import DonationRequest, Volunteer

admin.site.register(DonationRequest)
admin.site.register(Volunteer)