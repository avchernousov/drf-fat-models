def normalize_phone_prefix(phone):
    """Add "+" to phone prefix."""
    if phone is None:
        return None
    phone = str(phone)
    if phone == "":
        return None
    if not phone.startswith("+"):
        phone = "+" + phone
    return phone
