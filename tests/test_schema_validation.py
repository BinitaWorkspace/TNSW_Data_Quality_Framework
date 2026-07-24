import pytest

from src.validation.check_tables import check_table_exists
from src.utils.config_loader import load_config


config = load_config()


@pytest.mark.parametrize(
    "table_name",
    config["tables"]
)
def test_tables_exist(table_name):

    result = check_table_exists(
        table_name
    )

    print(result)

    assert result["status"] == "PASS"