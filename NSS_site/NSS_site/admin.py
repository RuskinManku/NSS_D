from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from .models import DonationRequest, VolunteerSlot


admin.site.register(DonationRequest)
admin.site.register(VolunteerSlot)
admin.site.site_header = 'NSS Donation Portal'


# class MyAdminSite(AdminSite):
#     # Text to put at the end of each page's <title>.
#     site_title = ugettext_lazy('NSS Donation Portal')

#     # Text to put in each page's <h1> (and above login form).
#     site_header = ugettext_lazy('Volunteer Section')

#     # Text to put at the top of the admin index page.
#     index_title = ugettext_lazy('NSS Donation Portal')

# admin_site = MyAdminSite()