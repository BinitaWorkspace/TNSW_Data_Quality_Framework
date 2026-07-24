from src.connection.destination_connection import get_destination_connection
from src.utils.config_loader import load_config
from src.utils.logger import get_logger


logger = get_logger(__name__)


def check_duplicate(table_name, column_name):

    conn = get_destination_connection()
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
        return f"PASS - No duplicate {column_name} in {table_name}"

    else:
        return f"FAIL - Duplicate {column_name}: {duplicates}"



def validate_all_duplicates():

    config = load_config()

    checks = config["duplicate_checks"]

    results = []

    for check in checks:

        table = check["table"]
        column = check["column"]

        results.append(
            check_duplicate(table, column)
        )

    return results