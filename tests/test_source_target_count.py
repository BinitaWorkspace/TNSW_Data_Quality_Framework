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
def test_source_target_row_count(table):

    result = validate_row_count(table)

    print("=" * 50)

    print("TABLE:", result["table"])

    print(
        "SOURCE COUNT:",
        result["source_count"]
    )

    print(
        "TARGET COUNT:",
        result["target_count"]
    )

    print(
        "STATUS:",
        result["status"]
    )

    assert result["status"] == "PASS"