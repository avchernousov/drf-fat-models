from helpers.utils import normalize_phone_prefix


class TestNormalizePhonePrefix:
    def test_none(self):
        assert normalize_phone_prefix(None) is None

    def test_empty(self):
        assert normalize_phone_prefix("") is None

    def test_7(self):
        assert normalize_phone_prefix("7") == "+7"

    def test_plus7(self):
        assert normalize_phone_prefix("+7") == "+7"

    def test_8(self):
        assert normalize_phone_prefix("8") == "+8"

    def test_plus8(self):
        assert normalize_phone_prefix("+8") == "+8"

    def test_61(self):
        assert normalize_phone_prefix("61") == "+61"

    def test_plus61(self):
        assert normalize_phone_prefix("+61") == "+61"

    def test_264(self):
        assert normalize_phone_prefix("264") == "+264"

    def test_plus264(self):
        assert normalize_phone_prefix("+264") == "+264"
