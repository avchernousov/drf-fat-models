# import pytest
# import pytz
# from django.utils import timezone
#
# from walks.enums import WalkStatus
# from walks.models import CancelWalkReason, Walk
#
# __all__ = ["create_cancel_reason", "create_walk"]
#
#
# @pytest.fixture
# def create_cancel_reason(request):
#     request.cls.cancel_reason1 = CancelWalkReason.objects.create(
#         name="name1", code="code1"
#     )
#     request.cls.cancel_reason2 = CancelWalkReason.objects.create(
#         name="name2", code="code2"
#     )
#
#
# @pytest.fixture
# def create_walk(
#     request,
#     create_users,
#     create_user_subscription,
#     create_pet,
#     create_pay_type,
#     create_cancel_reason,
# ):
#     request.cls.walk1 = Walk.objects.create(
#         customer=request.cls.user1,
#         executor=request.cls.user3,
#         walk_date=timezone.now() + timezone.timedelta(minutes=60),
#         duration=65,
#         price=100,
#         currency=Currency.RUB,
#         status=WalkStatus.OPEN,
#         address="address",
#         timezone=pytz.timezone("Europe/Moscow"),
#         location=Point(10, 10),
#         actual_start_time=timezone.now() - timezone.timedelta(minutes=10),
#         cancel_message="cancel_message",
#         cancel_reason=request.cls.cancel_reason1,
#     )
#     request.cls.walk1.pay_types.add(request.cls.pay_type1, request.cls.pay_type2)
#     request.cls.walk1.walk_pets.add(request.cls.pet1, request.cls.pet2)
#
#     request.cls.walk2 = Walk.objects.create(
#         customer=request.cls.user3,
#         executor=request.cls.user1,
#         walk_date=timezone.now() + timezone.timedelta(minutes=60),
#         duration=65,
#         price=110,
#         currency=Currency.RUB,
#         status=WalkStatus.OPEN,
#         address="address",
#         timezone=pytz.timezone("Europe/Moscow"),
#         location=Point(10, 10),
#         cancel_reason=request.cls.cancel_reason1,
#     )
#     request.cls.walk2.pay_types.add(request.cls.pay_type1)
#     request.cls.walk2.walk_pets.add(request.cls.pet1)
#
#     request.cls.walk3 = Walk.objects.create(
#         customer=request.cls.user2,
#         walk_date=timezone.now() + timezone.timedelta(minutes=60),
#         duration=65,
#         price=120,
#         currency=Currency.RUB,
#         status=WalkStatus.OPEN,
#         address="address",
#         timezone=pytz.timezone("Europe/Moscow"),
#         location=Point(10, 10),
#         cancel_reason=request.cls.cancel_reason1,
#     )
#     request.cls.walk3.walk_pets.add(request.cls.pet1)
