import os
from datetime import datetime
import pandas as pd


def generate_reports(results):

    if not os.path.exists("reports"):
        os.makedirs("reports")


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


    excel_file = (
        f"reports/data_quality_report_{timestamp}.xlsx"
    )

    html_file = (
        f"reports/data_quality_report_{timestamp}.html"
    )


    # Convert results to dataframe

    df = pd.DataFrame(results)


    # Excel Report

    with pd.ExcelWriter(
        excel_file,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="Validation Results",
            index=False
        )


    # HTML Report

    html_content = f"""
    <html>

    <head>
        <title>Data Quality Report</title>
    </head>

    <body>

    <h1>Oracle ATP Data Quality Report</h1>

    <p>
    Execution Time:
    {datetime.now()}
    </p>

    {df.to_html(index=False)}

    </body>

    </html>
    """


    with open(
        html_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html_content)


    return {
        "excel": excel_file,
        "html": html_file
    }