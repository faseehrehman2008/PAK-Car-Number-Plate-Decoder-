from database import PLATE_DATABASE
def decode_plate(prefix):
    return PLATE_DATABASE.get(prefix)