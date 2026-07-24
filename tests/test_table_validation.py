from src.validation.check_tables import check_table_exists


tables = [
    "PASSENGER",
    "TRIP",
    "BOOKING"
]


for table in tables:

    result = check_table_exists(table)

    print("=" * 50)
    print("TABLE:", result["table"])
    print("SOURCE EXISTS:", result["source_exists"])
    print("TARGET EXISTS:", result["target_exists"])
    print("STATUS:", result["status"])