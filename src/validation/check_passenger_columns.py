from src.connection.oracle_connection import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT column_name
FROM user_tab_columns
WHERE table_name = 'PASSENGER'
ORDER BY column_id
""")

print("PASSENGER columns:")

for row in cursor:
    print(row[0])

conn.close()