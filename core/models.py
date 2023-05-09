from django.contrib.gis.db import models
from django.conf import settings
from safedelete.models import SafeDeleteModel
from django.utils.translation import gettext_lazy as _
from safedelete.models import (
    SOFT_DELETE_CASCADE,
)


# Create your models here.
class TimedModel(models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TracedModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
        related_query_name="created_by_%(app_label)s_%(class)ss",
        verbose_name=_("Created by"),
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_updated_by",
        related_query_name="updated_by_%(app_label)s_%(class)ss",
        verbose_name=_("Updated by"),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class TracedSafeModel(SafeDeleteModel, TracedModel):
    class Meta:
        abstract = True


class TimedSafeModel(SafeDeleteModel, TimedModel):
    class Meta:
        abstract = True


class BaseModel(TracedModel, TimedModel):
    class Meta:
        abstract = True


class BaseSafeModel(SafeDeleteModel, TracedModel, TimedModel):
    class Meta:
        abstract = True
