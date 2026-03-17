import mysql.connector 

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Deb@2026prep",
        database = "product_db_learnbay"
    )
    print("Connection made")
    return conn