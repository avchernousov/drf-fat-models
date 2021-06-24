# import pytest
# from rest_framework.exceptions import ValidationError
#
# from ..models import CancelWalkReason
#
#
# @pytest.mark.usefixtures("create_cancel_reason")
# @pytest.mark.django_db
# class TestCancelWalkReasonModel:
#     def test_create(self):
#         CancelWalkReason.objects.create(name="name", code="code")
#         assert CancelWalkReason.objects.get(code="code").name == "name"
#
#     def test_update(self):
#         cancel_reason = CancelWalkReason.objects.get(code="code1")
#         cancel_reason.name = "test_name"
#         cancel_reason.save()
#         assert CancelWalkReason.objects.get(code="code1").name == "test_name"
#
#     def test_unique_name(self):
#         with pytest.raises(ValidationError):
#             CancelWalkReason.objects.create(name="name1", code="code")
#
#     def test_unique_code(self):
#         with pytest.raises(ValidationError):
#             CancelWalkReason.objects.create(name="name", code="code1")
#
#     def test_max_length_name(self):
#         with pytest.raises(ValidationError):
#             CancelWalkReason.objects.create(name="a" * 201, code="code1")
#
#     def test_max_length_code(self):
#         with pytest.raises(ValidationError):
#             CancelWalkReason.objects.create(name="name", code="a" * 51)
#
#     def test_delete(self):
#         row_num, _ = self.cancel_reason1.delete()
#         assert row_num == 1
