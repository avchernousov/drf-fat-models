import pytest
from rest_framework.exceptions import ValidationError

from apps.customers.models import Customer


@pytest.mark.django_db
class TestCustomerModel:
    def test_create_ok(self):
        Customer.objects.create(
            name="TestCustomer", is_verified=False, phone_prefix="61",
            phone_suffix="9003322233", email="testcustomer@example.com"
        )
        assert Customer.objects.get(name="TestCustomer").phone == "+619003322233"

    @pytest.mark.usefixtures("create_customers")
    def test_create_not_unique_phone(self):
        with pytest.raises(ValidationError) as exc_info:
            Customer.objects.create(
                name="TestCustomer", phone_prefix="7",
                phone_suffix="9003322233", email="TestCustomer@example.com"
            )
        assert exc_info.value.args[0] == {
            "phone_suffix": "User with this phone already exists."
        }

    @pytest.mark.usefixtures("create_customers")
    def test_update_email_required(self):
        customer = self.customer1
        customer.is_verified = True
        with pytest.raises(ValidationError) as exc_info:
            customer.save()
        assert exc_info.value.args[0] == {"email": "Email required for verified users"}
