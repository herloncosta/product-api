def data_validate(data):
    required_fields = ["name", "description", "price"]
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Field '{field}' is required."
    if not isinstance(data["price"], (float, int)) or data["price"] < 0:
        return False, "Field 'price' must be a positive number."
    return True, None
