from django.urls import path

from nilda_apps.core.views import index_view

app_name = 'core'

urlpatterns = [
    path('', index_view)
]