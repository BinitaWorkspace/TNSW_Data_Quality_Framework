import sys
import os
import pytest

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.connection.destination_connection import get_destination_connection

from src.validation.data_quality import (
    check_table_exists,
    check_row_count,
    check_null_values,
    check_duplicate_records
)

@pytest.fixture(scope="module")
def cursor():

    connection = get_destination_connection()
    cursor = connection.cursor()

    yield cursor

    cursor.close()
    connection.close()


def test_passenger_table_exists(cursor):

    result = check_table_exists(
        cursor,
        "PASSENGER"
    )

    assert result == "PASS"


def test_passenger_row_count(cursor):

    result = check_row_count(
        cursor,
        "PASSENGER"
    )

    assert result == "PASS"


def test_passenger_null_check(cursor):

    result = check_null_values(
        cursor,
        table_name="PASSENGER",
        column_name="PASSENGER_ID"
    )

    assert result == "PASS"


def test_passenger_duplicate_check(cursor):

    result = check_duplicate_records(
        cursor,
        table_name="PASSENGER",
        column_name="PASSENGER_ID"
    )

    assert result == "PASS"