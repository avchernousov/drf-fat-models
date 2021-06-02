from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models, transaction
from rest_framework.exceptions import ValidationError as DRFValidationError


class FatModel(models.Model):
    """Provides necessary methods for validation and actions before saving.

    The is_save_from_api instance flag can be used in validate_on_save, actions_on_save
    and prepare_on_save to check if the save is being executed from the DRF API (not
    from Django admin or forms).
    On validation errors raises DRF ValidationError if is_save_from_api is True,
    else - raises Django ValidationError.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Override model method."""
        self.is_save_from_api = getattr(self, "is_save_from_api", True)
        if self.is_save_from_api:
            self.full_clean()
        return super().save(*args, **kwargs)

    def full_clean(self, exclude=None, validate_unique=True):
        """Override model method."""

        def raise_exception(errors):
            validation_error = (
                DRFValidationError if self.is_save_from_api else DjangoValidationError
            )
            raise validation_error(errors)

        self.is_save_from_api = getattr(self, "is_save_from_api", False)
        errors = self.prepare_on_save()
        if errors:
            raise_exception(errors)

        try:
            super().full_clean(exclude=exclude, validate_unique=validate_unique)
        except DjangoValidationError as e:
            raise_exception(e.error_dict)

    def validate_on_save(self):
        """Validate model before save.

        Returns dictionary {field_name: error_str, ...} or error_str. Override this
        method if need.
        """
        return {}

    def actions_on_save(self):
        """Set model fields or update other models before save.

        Override this method if need.
        """
        pass

    def prepare_on_save(self):
        """Validate model and set model fields or update other models before save.

        Returns dictionary {field_name: error_str, ...} or error_str. Override this
        method in complex situations, for example if validation need AFTER actions.
        """
        errors = self.validate_on_save()
        if errors:
            return errors
        self.actions_on_save()
        return {}


class FatModelAtomic(FatModel):
    """Wraps the save into a transaction."""

    @transaction.atomic
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
