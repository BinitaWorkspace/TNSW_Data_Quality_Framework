from datetime import datetime
from src.connection.oracle_connection import get_connection


def load_passenger_data(data):

    conn = get_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO PASSENGER
    (
        PASSENGER_ID,
        FIRST_NAME,
        LAST_NAME,
        EMAIL,
        AGE,
        CREATED_DATE
    )
    VALUES
    (
        :1,
        :2,
        :3,
        :4,
        :5,
        :6
    )
    """

    cursor.executemany(
        insert_query,
        data
    )

    conn.commit()

    cursor.close()
    conn.close()

    print("PASSENGER data loaded successfully")


if __name__ == "__main__":

    sample_data = [
        (
            2001,
            "Test",
            "User",
            "test.user@example.com",
            30,
            datetime.now()
        )
    ]

    load_passenger_data(sample_data)