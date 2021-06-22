from django.db import models

from drf_fat_models import FatModelAtomic


class Customer(FatModelAtomic):
    name = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, unique=True)
    phone_prefix = models.CharField(max_length=10, verbose_name="Country code")
    phone_suffix = models.CharField(max_length=100, verbose_name="National number")

    # обязателен для is_verified
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def prepare_on_save(self):
        """Можно было бы обойтись validate_on_save и actions_on_save, но пришлось бы
        дважды вызывать normalize_phone_prefix в каждой из этих функций, либо где-то
        сохранять промежуточный результат."""
        errors = {}
        if self.is_verified and not self.email:
            errors["email"] = "Email required for verified users"

        self.phone = ""

        if self.phone_prefix and self.phone_suffix:
            self.phone_prefix = utils.normalize_phone_prefix(self.phone_prefix)

            phone = self.phone_prefix + self.phone_suffix

            temp_queryset = Customer.objects.filter(phone=phone)
            if self.pk is not None:
                # при редактировании пользователя исключаем себя
                temp_queryset = temp_queryset.exclude(id=self.pk)

            if temp_queryset.exists():
                errors["phone_suffix"] = "user with this phone already exists."
            else:
                self.phone = phone

        if errors:
            return errors
        return None
