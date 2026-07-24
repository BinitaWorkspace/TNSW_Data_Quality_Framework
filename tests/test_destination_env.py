from src.connection.destination_connection import get_destination_connection


conn = get_destination_connection()

cursor = conn.cursor()


cursor.execute("SELECT USER FROM dual")
print("USER:", cursor.fetchone())


cursor.execute(
    "SELECT SYS_CONTEXT('USERENV','SERVICE_NAME') FROM dual"
)
print("SERVICE:", cursor.fetchone())


cursor.execute(
    "SELECT SYS_CONTEXT('USERENV','AUTHENTICATION_METHOD') FROM dual"
)
print("AUTH:", cursor.fetchone())


conn.close()

print("Destination DB connection successful")