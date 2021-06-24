from django.db import models

from drf_fat_models import FatModelAtomic


class Order(FatModelAtomic):
    DRAFT, OPENED, CLOSED = range(3)
    STATUSES = (
        (DRAFT, "DRAFT"),
        (OPENED, "OPENED"),
        (CLOSED, "CLOSED"),
    )
    status = models.IntegerField(choices=STATUSES)
    order_date = models.DateTimeField()
    description = models.TextField()
    customer = models.ForeignKey(
        "customers.User",
        on_delete=models.PROTECT,
        verbose_name=_("Customer"),
        related_name="customer_walks",
    )
