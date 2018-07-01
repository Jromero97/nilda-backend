from django.contrib import admin

# Register your models here.
from nilda_apps.ethnic.models import EthnicGroup


@admin.register(EthnicGroup)
class EthnicGroupAdmin(admin.ModelAdmin):
    pass
