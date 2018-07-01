from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speciality(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.CharField(max_length=255, verbose_name=_('description'))

    def __str__(self):
        return 'Speciality: ' + self.name

    class Meta:
        verbose_name_plural = _('Specialities')
