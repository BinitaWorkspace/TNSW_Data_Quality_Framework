from src.connection.source_connection import get_source_connection
from src.connection.destination_connection import get_destination_connection


PRIMARY_KEYS = {
    "PASSENGER": "PASSENGER_ID",
    "TRIP": "TRIP_ID",
    "STATION": "STATION_ID",
    "BOOKING": "BOOKING_ID"
}


def reconcile_table(table_name):

    primary_key = PRIMARY_KEYS[table_name.upper()]

    source_conn = get_source_connection()
    target_conn = get_destination_connection()

    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()

    # Fetch source data
    source_cursor.execute(
        f"SELECT * FROM {table_name}"
    )

    source_columns = [
        col[0] for col in source_cursor.description
    ]

    source_rows = source_cursor.fetchall()


    # Fetch target data
    target_cursor.execute(
        f"SELECT * FROM {table_name}"
    )

    target_columns = [
        col[0] for col in target_cursor.description
    ]

    target_rows = target_cursor.fetchall()


    # Convert rows into dictionaries using primary key

    source_data = {
        row[source_columns.index(primary_key)]: row
        for row in source_rows
    }

    target_data = {
        row[target_columns.index(primary_key)]: row
        for row in target_rows
    }


    missing_in_target = (
        set(source_data.keys())
        - set(target_data.keys())
    )

    extra_in_target = (
        set(target_data.keys())
        - set(source_data.keys())
    )


    mismatches = []

    for key in source_data.keys() & target_data.keys():

        if source_data[key] != target_data[key]:
            mismatches.append(key)


    source_conn.close()
    target_conn.close()


    return {
        "table": table_name,
        "source_count": len(source_rows),
        "target_count": len(target_rows),
        "missing_in_target": list(missing_in_target),
        "extra_in_target": list(extra_in_target),
        "data_mismatch": mismatches,
        "status": "PASS"
        if not missing_in_target
        and not extra_in_target
        and not mismatches
        else "FAIL"
    }