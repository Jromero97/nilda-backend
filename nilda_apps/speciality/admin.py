from django.contrib import admin

# Register your models here.
from nilda_apps.speciality.models import Speciality


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass
