from src.connection.oracle_connection import get_connection


def check_table_exists(cursor, table_name):

    cursor.execute("""
        SELECT COUNT(*)
        FROM user_tables
        WHERE table_name = :table_name
    """, {"table_name": table_name.upper()})

    result = cursor.fetchone()[0]

    return "PASS" if result == 1 else "FAIL"


def check_row_count(cursor, table_name):

    cursor.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    )

    count = cursor.fetchone()[0]

    return f"PASS - {count} records" if count > 0 else "FAIL"


if __name__ == "__main__":

    conn = get_connection()
    cursor = conn.cursor()

    print(
        "PASSENGER table check:",
        check_table_exists(cursor, "PASSENGER")
    )

    print(
        "TRIP row count check:",
        check_row_count(cursor, "TRIP")
    )

    print(
        "BOOKING row count check:",
        check_row_count(cursor, "BOOKING")
    )

    conn.close()