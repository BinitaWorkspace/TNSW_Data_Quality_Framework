from src.connection.oracle_connection import get_connection


def check_booking_business_rules():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT BOOKING_ID
    FROM BOOKING
    WHERE STATUS = 'CONFIRMED'
    AND (TICKET_PRICE IS NULL OR TICKET_PRICE <= 0)
    """

    cursor.execute(query)

    invalid_records = cursor.fetchall()

    conn.close()

    if len(invalid_records) == 0:
        return "PASS - All confirmed bookings have valid ticket prices"
    else:
        return f"FAIL - Confirmed bookings with invalid ticket price: {invalid_records}"


if __name__ == "__main__":

    result = check_booking_business_rules()
    print(result)