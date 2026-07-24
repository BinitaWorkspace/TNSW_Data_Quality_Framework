import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

# Initialize Thick mode ONLY ONCE
oracledb.init_oracle_client(
    lib_dir=r"C:/app/Home/product/21c/dbhomeXE/bin",
    config_dir=os.getenv("WALLET_LOCATION")
)

def get_destination_connection():

    connection = oracledb.connect(
        user=os.getenv("TARGET_DB_USER"),
        password=os.getenv("TARGET_DB_PASSWORD"),
        dsn=os.getenv("TARGET_DB_DSN")
    )

    return connection