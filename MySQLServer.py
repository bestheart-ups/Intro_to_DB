import mysql.connector 
from mysql.connector import Error 

def create_database():
    try:
        # Connect to MySQL server (adjust user and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',
            password='your_mysql_password'  # Replace with your MySQL root password
        )
        cursor = connection.cursor()

        # Create database if not exists (no SELECT or SHOW statements used)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        else:
            print(f"Error: {err}")
    finally:
        # Close cursor and connection properly
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()