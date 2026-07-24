from src.connection.source_connection import get_source_connection
from src.connection.destination_connection import get_destination_connection


def check_table_exists(table_name):

    source_conn = get_source_connection()
    target_conn = get_destination_connection()

    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()

    source_cursor.execute("""
    SELECT COUNT(*)
    FROM USER_TABLES
    WHERE TABLE_NAME = :tbl_name
    """, {"tbl_name": table_name.upper()})

    source_exists = source_cursor.fetchone()[0] > 0


    target_cursor.execute(
        """
        SELECT COUNT(*)
        FROM USER_TABLES
        WHERE TABLE_NAME = :tbl_name
        """,
        {"tbl_name": table_name.upper()}
    )

    target_exists = target_cursor.fetchone()[0] > 0


    source_conn.close()
    target_conn.close()


    return {
        "table": table_name,
        "source_exists": source_exists,
        "target_exists": target_exists,
        "status": "PASS"
        if source_exists and target_exists
        else "FAIL"
    }