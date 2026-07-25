def validate_plate_number(plate):
    plate = plate.strip().upper()

    if "_" not in plate:
        return False, None, None

    prefix, number = plate.split("_", 1)

    if len(prefix) < 2 or not number.isdigit():
        return False, None, None

    return True, prefix, number