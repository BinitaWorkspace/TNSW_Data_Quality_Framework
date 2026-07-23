from src.connection.oracle_connection import get_connection


def get_row_count(cursor, table_name):

    query = f"SELECT COUNT(*) FROM {table_name}"

    cursor.execute(query)

    return cursor.fetchone()[0]


if __name__ == "__main__":

    conn = get_connection()

    cursor = conn.cursor()

    tables = [
        "PASSENGER",
        "TRIP",
        "BOOKING"
    ]

    for table in tables:

        count = get_row_count(cursor, table)

        print(
            f"{table} row count: {count}"
        )

    conn.close()