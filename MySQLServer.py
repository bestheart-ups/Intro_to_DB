import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (not a specific DB yet)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',      # <-- Replace this
            password='your_mysql_password'   # <-- Replace this
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()
                connection.close()
                print("MySQL connection closed.")

    except mysql.connector.Error as e:
        print(f"Failed to connect to MySQL: {e}")

if __name__ == "__main__":
    create_database()