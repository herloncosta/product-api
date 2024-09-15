def data_validate(data):
    required_fields = ["name", "email", "password", "role"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Field '{field}' is required."
    return True, None
