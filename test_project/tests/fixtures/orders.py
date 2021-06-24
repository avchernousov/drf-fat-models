import pytest

from apps.orders.models import Order


@pytest.fixture
def create_orders(request, create_customers):
    request.cls.order1 = Order.objects.create(
        description="Description 1",
        customer=request.cls.customer1
    )
    request.cls.order2 = Order.objects.create(
        description="Description 2",
        customer=request.cls.customer2
    )
