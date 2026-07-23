from src.validation.relationship_validator import validate_booking_trip_relationship


def test_booking_trip_relationship():

    result = validate_booking_trip_relationship()

    print(result)

    assert result == "PASS"