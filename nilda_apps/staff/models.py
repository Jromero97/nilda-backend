from django.db import models
from django.utils.translation import ugettext_lazy as _


class Staff(models.Model):
    """
    This model define a staff into the hospital
    Could be a Doctor, Nurse or Nursery Aux.
    """
    SEX_CHOICES = [
        ('F', _('Female')),
        ('M', _('Male'))
    ]

    dni = models.CharField(max_length=255, verbose_name=_('DNI'))
    first_name = models.CharField(max_length=255, verbose_name=_('first Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last Name'))
    address = models.CharField(max_length=255, verbose_name=_('address'))
    email = models.EmailField(max_length=255, verbose_name=_('e-mail'))
    phone = models.CharField(max_length=255, verbose_name=_('phone Number'))
    born_date = models.DateField(verbose_name=_('born Date'))
    age = models.IntegerField(verbose_name=_('age'))
    sex = models.CharField(verbose_name=_('sex'), choices=SEX_CHOICES, max_length=2)
    minsa_code = models.CharField(max_length=20, verbose_name=_('MINSA Code'))

    def __str__(self):
        return 'Staff: ' + self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = _('Staff member')
        verbose_name_plural = _('Staff members')
