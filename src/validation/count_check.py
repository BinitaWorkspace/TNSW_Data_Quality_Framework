from src.connection.oracle_connection import get_connection
from src.utils.logger import get_logger

logger = get_logger(__name__)


def check_row_count(table_name):

    logger.info(f"Starting row count validation for {table_name}")

    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT COUNT(*)
    FROM {table_name}
    """

    cursor.execute(query)

    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    if count > 0:
        result = f"PASS - {table_name} has {count} records"
    else:
        result = f"FAIL - {table_name} is empty"

    logger.info(result)

    return result


def validate_all_row_counts():

    tables = [
        "PASSENGER",
        "TRIP",
        "BOOKING",
        "STATION"
    ]

    results = []

    logger.info("Starting row count validation")

    for table in tables:
        results.append(check_row_count(table))

    logger.info("Row count validation completed")

    return results


if __name__ == "__main__":

    results = validate_all_row_counts()

    for result in results:
        print(result)