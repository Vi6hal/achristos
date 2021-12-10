import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from devutils.models import AbstractModel

class AppRegistery(AbstractModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    url = models.URLField(unique=True)
    last_pinged = models.DateTimeField(_("Last Seen"),blank=True,null=True)
    bedtime = models.BooleanField(_("Allow bedtime"),default=False)

    class Meta:
        verbose_name = "app"
        verbose_name_plural = "Coldbrew apps"