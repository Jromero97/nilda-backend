from django.contrib import admin

from nilda_apps.charge.models import StaffCharge


@admin.register(StaffCharge)
class StaffChargeAdmin(admin.ModelAdmin):
    pass
