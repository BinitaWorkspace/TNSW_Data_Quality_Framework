from src.connection.oracle_connection import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
DELETE FROM PASSENGER
WHERE PASSENGER_ID = 2001
""")

conn.commit()

cursor.close()
conn.close()

print("Test data removed")