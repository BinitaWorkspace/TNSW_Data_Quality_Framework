from src.connection.source_connection import get_source_connection
from src.connection.destination_connection import get_destination_connection


def get_count(connection, table_name):

    cursor = connection.cursor()

    cursor.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    )

    count = cursor.fetchone()[0]

    cursor.close()

    return count


def validate_row_count(table_name):

    source_conn = get_source_connection()
    target_conn = get_destination_connection()

    source_count = get_count(
        source_conn,
        table_name
    )

    target_count = get_count(
        target_conn,
        table_name
    )

    source_conn.close()
    target_conn.close()


    result = {
        "table": table_name,
        "source_count": source_count,
        "target_count": target_count,
        "status": (
            "PASS"
            if source_count == target_count
            else "FAIL"
        )
    }

    return result