from django.db import models


class TimeStampedModel(models.Model):
    """
    TimeStampedModel

    An abstract base class model that provides self-managed "create_date" and
    "update_date" fields.
    """

    create_date = models.DateTimeField(
        editable=False, blank=True, auto_now=True,
    )
    update_date = models.DateTimeField(
        editable=False, blank=True, auto_now_add=True,
    )

    class Meta:
        get_latest_by = 'create_date'
        ordering = ('create_date',)
        abstract = True
