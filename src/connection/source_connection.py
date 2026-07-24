import oracledb
import os
from dotenv import load_dotenv

load_dotenv()


def get_source_connection():

    connection = oracledb.connect(
        user=os.getenv("SOURCE_DB_USER"),
        password=os.getenv("SOURCE_DB_PASSWORD"),
        dsn=os.getenv("SOURCE_DB_DSN")
    )

    return connection