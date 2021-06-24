import pytest
from rest_framework.exceptions import ValidationError

from apps.orders.models import Order


@pytest.mark.django_db
class TestOrderModel:
    @pytest.mark.usefixtures("create_customers")
    def test_create_not_verified_ok(self):
        order = Order.objects.create(
            description="Description", customer=self.customer1
        )
        assert order.status == Order.DRAFT

    @pytest.mark.usefixtures("create_customers")
    def test_create_verified_ok(self):
        order = Order.objects.create(
            description="Description", customer=self.customer2
        )
        assert order.status == Order.OPENED

    @pytest.mark.usefixtures("create_orders")
    def test_update_status_opened_ok(self):
        order = self.order1
        order.status = Order.OPENED
        order.save()
        assert order.status == Order.OPENED

    @pytest.mark.usefixtures("create_orders")
    def test_update_status_opened_bad(self):
        order = self.order2
        order.status = Order.OPENED
        with pytest.raises(ValidationError) as exc_info:
            order.save()
        assert exc_info.value.args[0] == "This status cannot be set"
