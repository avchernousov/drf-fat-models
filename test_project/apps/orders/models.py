from django.db import models

from drf_fat_models import FatModel
from rest_framework.generics import get_object_or_404


class Order(FatModel):
    DRAFT, OPENED, CLOSED = range(3)
    STATUSES = (
        (DRAFT, "DRAFT"),
        (OPENED, "OPENED"),
        (CLOSED, "CLOSED"),
    )
    status = models.IntegerField(choices=STATUSES)
    order_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    customer = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)

    def __str__(self):
        return f"Order id={self.pk} of {self.customer}"

    def validate_on_save(self):
        """Validate model before saving.

        On error, it must return dictionary {field_name: error_str, ...}
        or error string, on success - empty dictionary or None.

        When editing from the API, you cannot change the status to DRAFT, but from the
        admin panel and forms you can.
        """
        if self.pk and self.is_save_from_api:
            old_order = get_object_or_404(Order.objects.all(), pk=self.pk)
            if old_order.status != self.DRAFT and self.status == self.OPENED:
                return "This status cannot be set"

    def actions_on_save(self):
        """Perform arbitrary actions after validation before saving.

        We change the status to DRAFT when creating an order for an unverified customer.
        """
        if self.pk is None:
            self.status = self.OPENED
            customer = self.customer
            if customer and not customer.is_verified:
                self.status = self.DRAFT
