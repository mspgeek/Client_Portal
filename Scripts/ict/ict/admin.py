from django.contrib import admin

from .models import Firewall_Brand, Firewall_Model,OnboardingWizard,ContactInformation,NetworkInformation

class ContactAdmin(admin.ModelAdmin):

    list_display = ['id','contact_id','contact_firstname','contact_lastname','contact_type','onboarding_id']

class NetworkAdmin(admin.ModelAdmin):

    list_display = ['id','onboarding_id','type','brand','model','replace']


admin.site.register(NetworkInformation, NetworkAdmin)
admin.site.register(Firewall_Brand)
admin.site.register(Firewall_Model)
admin.site.register(OnboardingWizard)
admin.site.register(ContactInformation, ContactAdmin)