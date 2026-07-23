from src.validation.check_tables import validate_tables_exist


def test_schema_tables():

    result = validate_tables_exist()

    print(result)

    assert "FAIL" not in result