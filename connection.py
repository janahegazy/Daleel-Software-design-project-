import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx

    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="janahegazy2372005",
                database="daleel"
            )
            print("✅ MySQL Connected Successfully!")
        except mysql.connector.Error as err:
            print("❌ Connection Failed:", err)

    return __cnx