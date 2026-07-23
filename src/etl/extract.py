from src.connection.oracle_connection import get_connection


def extract_table_data(table_name):

    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT *
    FROM {table_name}
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = [col[0] for col in cursor.description]

    conn.close()

    return columns, rows


if __name__ == "__main__":

    columns, data = extract_table_data("PASSENGER")

    print("Columns:")
    print(columns)

    print("Records:")
    for row in data:
        print(row)