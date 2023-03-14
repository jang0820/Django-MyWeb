from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'), help_text=_('job title'))
    finish = models.BooleanField(default=False, verbose_name=_('finished'), help_text=_('does job finish'))
    created = models.DateField(default=timezone.now)
