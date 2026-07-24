
from src.connection.destination_connection import get_destination_connection

def check_null_values(table_name, column_name):

    conn = get_destination_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT COUNT(*)
    FROM {table_name}
    WHERE {column_name} IS NULL
    """

    cursor.execute(query)

    null_count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    if null_count == 0:
        return f"PASS - No NULL values in {table_name}.{column_name}"
    else:
        return f"FAIL - {null_count} NULL values found in {table_name}.{column_name}"


def validate_all_null_checks():

    checks = [
        ("PASSENGER", "PASSENGER_ID"),
        ("BOOKING", "BOOKING_ID"),
        ("BOOKING", "TICKET_PRICE"),
        ("TRIP", "TRIP_ID"),
        ("STATION", "STATION_ID")
    ]

    results = []

    for table, column in checks:
        result = check_null_values(table, column)
        results.append(result)

    return results


if __name__ == "__main__":

    results = validate_all_null_checks()

    for result in results:
        print(result)