from src.connection.oracle_connection import get_connection


def check_booking_trip_relationship():

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

    invalid_count = cursor.fetchone()[0]

    conn.close()

    if invalid_count == 0:
        return "PASS - All bookings have valid trips"
    else:
        return f"FAIL - {invalid_count} bookings have invalid TRIP_ID"


if __name__ == "__main__":

    result = check_booking_trip_relationship()

    print(result)