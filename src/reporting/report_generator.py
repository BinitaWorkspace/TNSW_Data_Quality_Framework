from datetime import datetime
import os


def generate_report(results):

    os.makedirs("reports", exist_ok=True)

    file_name = (
        f"reports/data_quality_report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(file_name, "w") as report:

        report.write("DATA QUALITY VALIDATION REPORT\n")
        report.write("=" * 40)
        report.write("\n")
        report.write(
            f"Execution Time: {datetime.now()}\n\n"
        )

        for result in results:
            report.write(result)
            report.write("\n")

    print(f"Report generated: {file_name}")


if __name__ == "__main__":

    validation_results = [
        "PASS - Tables exist",
        "PASS - PASSENGER has 4 records",
        "PASS - No duplicate booking IDs",
        "FAIL - Confirmed booking 5003 has NULL ticket price"
    ]

    generate_report(validation_results)