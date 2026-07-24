from src.validation.data_reconciliation import reconcile_table


tables = [
    "PASSENGER",
    "TRIP",
    "BOOKING",
    "STATION"
]


for table in tables:

    result = reconcile_table(table)

    print("=" * 50)
    print("TABLE:", result["table"])
    print("SOURCE COUNT:", result["source_count"])
    print("TARGET COUNT:", result["target_count"])
    print("MISSING:", result["missing_in_target"])
    print("EXTRA:", result["extra_in_target"])
    print("MISMATCH:", result["data_mismatch"])
    print("STATUS:", result["status"])