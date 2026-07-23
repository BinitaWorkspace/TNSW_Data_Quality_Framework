from src.validation.null_check import validate_all_null_checks


def test_null_validation():

    results = validate_all_null_checks()

    for result in results:
        print(result)

        assert "FAIL" not in result