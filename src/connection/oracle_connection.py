import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

wallet = os.getenv("WALLET_LOCATION")

print("Wallet:", wallet)

oracledb.defaults.config_dir = wallet


def get_connection():

    connection = oracledb.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dsn=os.getenv("DB_DSN"),
    config_dir=os.getenv("WALLET_LOCATION"),
    wallet_location=os.getenv("WALLET_LOCATION")
    )

    return connection


if __name__ == "__main__":

    conn = get_connection()

    print("Oracle Connection Successful")

    conn.close()