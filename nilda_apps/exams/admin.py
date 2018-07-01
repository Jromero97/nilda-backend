from django.contrib import admin

# Register your models here.
from nilda_apps.exams.models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass
