from django.contrib import admin

# Register your models here.
from nilda_apps.medicine.models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    pass
