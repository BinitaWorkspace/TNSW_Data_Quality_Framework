from src.connection.oracle_connection import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT column_name
FROM user_tab_columns
WHERE table_name = 'BOOKING'
ORDER BY column_id
""")

print("BOOKING columns:")

for row in cursor:
    print(row[0])

conn.close()