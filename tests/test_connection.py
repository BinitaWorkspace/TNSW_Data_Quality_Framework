from src.connection.oracle_connection import get_connection
print(get_connection)


def test_oracle_connection():

    connection = get_connection()

    assert connection is not None

    connection.close()