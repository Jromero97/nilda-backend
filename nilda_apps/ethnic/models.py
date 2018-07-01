from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class EthnicGroup(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)

    def __str__(self):
        return self.name
