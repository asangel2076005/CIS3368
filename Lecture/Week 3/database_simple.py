import mysql.connector
from mysql.connector import Error


def create_con(hostname, username, user_password, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=user_password,
            database=dbname
        )
        print("Connection Success")

    except Error as e:
        print(f"The error {e} occurred")

    return connection


if __name__ == "__main__":
    conn = create_con("cis3368spring.cb0eqkk045ol.us-east-1.rds.amazonaws.com",
                      "angeloangel",
                      "serdon17",
                      "cis3368springdb")

    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM users"  # String we want to deliver
    
    cursor.execute(sql)
    rows = cursor.fetchall()

    for user in rows:
        print(user)
