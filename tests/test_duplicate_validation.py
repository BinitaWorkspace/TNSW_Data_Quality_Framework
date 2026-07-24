import pytest

from src.connection.destination_connection import get_destination_connection

from src.validation.data_quality import check_duplicate_records

from src.utils.config_loader import load_config


config = load_config()


@pytest.fixture(scope="module")
def cursor():

    connection = get_destination_connection()
    cursor = connection.cursor()

    yield cursor

    cursor.close()
    connection.close()


@pytest.mark.parametrize(
    "duplicate_check",
    config["duplicate_checks"]
)
def test_duplicate_checks(cursor, duplicate_check):

    result = check_duplicate_records(
        cursor,
        duplicate_check["table"],
        duplicate_check["column"]
    )

    assert result == "PASS"