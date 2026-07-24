import pytest

from src.validation.source_target_count_validation import validate_row_count


tables = [
    "PASSENGER",
    "TRIP",
    "BOOKING"
]


@pytest.mark.parametrize(
    "table",
    tables
)
def test_row_counts(table):

    result = validate_row_count(table)

    print(result)

    assert result["status"] != "FAIL"