from src.connection.oracle_connection import get_connection


def check_duplicate(table_name, column_name):

    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT {column_name}, COUNT(*)
    FROM {table_name}
    GROUP BY {column_name}
    HAVING COUNT(*) > 1
    """

    cursor.execute(query)

    duplicates = cursor.fetchall()

    cursor.close()
    conn.close()

    if len(duplicates) == 0:
        return f"PASS - No duplicate {table_name}.{column_name}"
    else:
        return f"FAIL - Duplicate {table_name}.{column_name} found: {duplicates}"


def validate_all_duplicates():

    checks = [
        ("PASSENGER", "PASSENGER_ID"),
        ("TRIP", "TRIP_ID"),
        ("BOOKING", "BOOKING_ID"),
        ("STATION", "STATION_ID")
    ]

    results = []

    for table, column in checks:
        result = check_duplicate(table, column)
        results.append(result)

    return results


if __name__ == "__main__":

    results = validate_all_duplicates()

    for result in results:
        print(result)