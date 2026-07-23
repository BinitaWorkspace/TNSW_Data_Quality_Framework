from src.utils.logger import get_logger

from src.validation.check_tables import validate_tables_exist
from src.validation.count_check import validate_all_row_counts
from src.validation.duplicate_check import validate_all_duplicates
from src.validation.null_check import validate_all_null_checks
from src.validation.relationship_validator import validate_booking_trip_relationship
from src.validation.business_rules import check_booking_business_rules
from src.reporting.report_generator import generate_report

logger = get_logger(__name__)


def run_data_quality_framework():

    logger.info("========== DATA QUALITY FRAMEWORK STARTED ==========")

    results = []


    # 1. Schema Validation
    logger.info("Running schema validation")

    schema_result = validate_tables_exist()

    results.append(
        {
            "Validation": "Schema Validation",
            "Result": schema_result
        }
    )


    # 2. Row Count Validation
    logger.info("Running row count validation")

    row_results = validate_all_row_counts()

    for result in row_results:
        results.append(
            {
                "Validation": "Row Count",
                "Result": result
            }
        )


    # 3. Duplicate Validation
    logger.info("Running duplicate validation")

    duplicate_results = validate_all_duplicates()

    for result in duplicate_results:
        results.append(
            {
                "Validation": "Duplicate Check",
                "Result": result
            }
        )


    # 4. Null Validation
    logger.info("Running null validation")

    null_results = validate_all_null_checks()

    for result in null_results:
        results.append(
            {
                "Validation": "Null Check",
                "Result": result
            }
        )


    # 5. Relationship Validation
    logger.info("Running relationship validation")

    relationship_result = validate_booking_trip_relationship()

    results.append(
        {
            "Validation": "Relationship Check",
            "Result": relationship_result
        }
    )


    # 6. Business Rules
    logger.info("Running business rule validation")

    business_result = check_booking_business_rules()

    results.append(
        {
            "Validation": "Business Rules",
            "Result": business_result
        }
    )


    logger.info("========== DATA QUALITY FRAMEWORK COMPLETED ==========")

    return results



if __name__ == "__main__":

    execution_results = run_data_quality_framework()


    print("\n===== DATA QUALITY EXECUTION REPORT =====")


report_files = generate_reports(execution_results)


logger.info(
    f"Excel report: {report_files['excel']}"
)

logger.info(
    f"HTML report: {report_files['html']}"
)