from src.validation.duplicate_check import validate_all_duplicates


def test_duplicate_validation():

    results = validate_all_duplicates()

    for result in results:
        assert "FAIL" not in result