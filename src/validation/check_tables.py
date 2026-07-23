from src.connection.oracle_connection import get_connection


def check_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name
        FROM user_tables
        ORDER BY table_name
    """)

    tables = cursor.fetchall()

    cursor.close()
    conn.close()

    return [table[0] for table in tables]


def validate_tables_exist():

    expected_tables = [
        "PASSENGER",
        "TRIP",
        "BOOKING",
        "STATION"
    ]

    existing_tables = check_tables()

    missing_tables = [
        table for table in expected_tables
        if table not in existing_tables
    ]

    if not missing_tables:
        return "PASS - All expected tables exist"

    return f"FAIL - Missing tables: {missing_tables}"


if __name__ == "__main__":

    print("Tables in TFNSW_TEST schema:")

    for table in check_tables():
        print(table)

    print(validate_tables_exist())