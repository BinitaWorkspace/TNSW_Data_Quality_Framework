from src.connection.oracle_connection import get_connection


def validate_booking_trip_relationship():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM BOOKING b
    LEFT JOIN TRIP t
    ON b.TRIP_ID = t.TRIP_ID
    WHERE t.TRIP_ID IS NULL
    """

    cursor.execute(query)

    invalid_records = cursor.fetchone()[0]

    conn.close()

    if invalid_records == 0:
        return "PASS"
    else:
        return f"FAIL - {invalid_records} invalid bookings"


if __name__ == "__main__":
    print(validate_booking_trip_relationship())