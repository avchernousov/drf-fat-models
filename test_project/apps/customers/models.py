from django.db import models

from drf_fat_models import FatModel
from helpers import utils


class Customer(FatModel):
    name = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=110, unique=True)
    phone_prefix = models.CharField(max_length=10, verbose_name="Country code")
    phone_suffix = models.CharField(max_length=100, verbose_name="National number")

    # email required for verified customers
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"Customer {self.name} {'(unverified)' if not self.is_verified else ''}"

    def prepare_on_save(self):
        """Validate model and perform arbitrary actions before saving.

        On error, it must return dictionary {field_name: error_str, ...}
        or error string, on success - empty dictionary or None.

        Override this method in complex situations, for example if validation need
        AFTER actions. For simple situations see Orders model.

        You could get by with validate_on_save and actions_on_save, but you would
        have to call normalize_phone_prefix twice in each of these functions, or save
        the intermediate result somewhere.
        """
        errors = {}
        if self.is_verified and not self.email:
            errors["email"] = "Email required for verified users"

        self.phone = ""

        if self.phone_prefix and self.phone_suffix:
            self.phone_prefix = utils.normalize_phone_prefix(self.phone_prefix)

            phone = self.phone_prefix + self.phone_suffix

            temp_queryset = Customer.objects.filter(phone=phone)
            if self.pk is not None:
                # when editing a user, we exclude ourselves
                temp_queryset = temp_queryset.exclude(id=self.pk)

            if temp_queryset.exists():
                errors["phone_suffix"] = "User with this phone already exists"
            else:
                self.phone = phone

        if errors:
            return errors
        return None
