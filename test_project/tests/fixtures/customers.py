import pytest

from test_project.apps.customers.models import Customer


@pytest.fixture
def create_customers(request):
    request.cls.customer1 = Customer.objects.create(
        name="Customer1", phone_prefix="+7", phone_suffix="9003322233"
    )
    request.cls.customer2 = Customer.objects.create(
        name="Customer2", is_verified=True, phone_prefix="+1",
        phone_suffix="9003322233", email="customer2@example.com"
    )
