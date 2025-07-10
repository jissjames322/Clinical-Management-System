from django.contrib import admin
from rootapp.models import Patient, Membership

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('PatientId', 'PatientName', 'MobileNumber', 'MembershipId', 'IsActive')
    list_filter = ('MembershipId', 'IsActive')
    search_fields = ('PatientName', 'MobileNumber')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('MembershipId', 'MembershipType', 'IsActive')
    list_filter = ('IsActive',)