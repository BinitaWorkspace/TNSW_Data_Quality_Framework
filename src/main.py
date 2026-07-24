from validation.count_check import run_count_check
from validation.null_check import run_null_check
from validation.duplicate_check import run_duplicate_check
from validation.relationship_validator import run_relationship_check


def main():

    tables = [
        "PASSENGER",
        "TRIP",
        "BOOKING"
    ]

    results = []

    print("=" * 60)
    print("SOURCE TO TARGET DATA QUALITY VALIDATION")
    print("=" * 60)


    for table in tables:

        print(f"\nRunning validations for {table}")

        results.append(
            run_count_check(table)
        )

        results.append(
            run_null_check(table)
        )

        results.append(
            run_duplicate_check(table)
        )


    print("\nVALIDATION COMPLETED")

    print("=" * 60)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()