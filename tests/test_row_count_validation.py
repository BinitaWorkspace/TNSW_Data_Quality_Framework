from src.validation.count_check import validate_all_row_counts


def test_row_counts():

    results = validate_all_row_counts()

    for result in results:
        print(result)

        assert "FAIL" not in result