from django.contrib import admin

# Register your models here.
from nilda_apps.pathology.models import Pathology


@admin.register(Pathology)
class PathologyAdmin(admin.ModelAdmin):
    pass
