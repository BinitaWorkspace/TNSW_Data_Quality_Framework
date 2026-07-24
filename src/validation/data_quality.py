from datetime import datetime


def check_table_exists(cursor, table_name):
    """
    Check whether table exists in Oracle schema
    """

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM user_tables
        WHERE table_name = :table_name
        """,
        {
            "table_name": table_name.upper()
        }
    )

    result = cursor.fetchone()[0]

    return "PASS" if result == 1 else "FAIL"


def check_row_count(cursor, table_name):
    """
    Validate table has records
    """

    query = f"""
        SELECT COUNT(*)
        FROM {table_name}
    """

    cursor.execute(query)

    count = cursor.fetchone()[0]

    return "PASS" if count > 0 else "FAIL"


def check_null_values(cursor, table_name, column_name):
    """
    Check mandatory column does not contain NULL values
    """

    query = f"""
        SELECT COUNT(*)
        FROM {table_name}
        WHERE {column_name} IS NULL
    """

    cursor.execute(query)

    null_count = cursor.fetchone()[0]

    return "PASS" if null_count == 0 else "FAIL"


def check_duplicate_records(cursor, table_name, column_name):
    """
    Check duplicate primary key values
    """

    query = f"""
        SELECT COUNT(*)
        FROM (
            SELECT {column_name}
            FROM {table_name}
            GROUP BY {column_name}
            HAVING COUNT(*) > 1
        )
    """

    cursor.execute(query)

    duplicate_count = cursor.fetchone()[0]

    return "PASS" if duplicate_count == 0 else "FAIL"


def check_record_count_match(cursor, source_count, target_count):
    """
    Compare source and target row counts
    """

    return "PASS" if source_count == target_count else "FAIL"


def check_foreign_key_integrity(
        cursor,
        child_table,
        child_column,
        parent_table,
        parent_column
):
    """
    Validate foreign key relationship
    """

    query = f"""
        SELECT COUNT(*)
        FROM {child_table} c
        LEFT JOIN {parent_table} p
        ON c.{child_column} = p.{parent_column}
        WHERE p.{parent_column} IS NULL
    """

    cursor.execute(query)

    invalid_count = cursor.fetchone()[0]

    return "PASS" if invalid_count == 0 else "FAIL"


def generate_validation_result(
        check_name,
        table_name,
        status
):
    """
    Generate validation result dictionary
    for reporting
    """

    return {
        "check_name": check_name,
        "table_name": table_name,
        "status": status,
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }