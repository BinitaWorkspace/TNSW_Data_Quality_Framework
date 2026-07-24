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