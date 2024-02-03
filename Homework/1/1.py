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

    except Error as e:
        print(f"The error {e} occurred")

    return connection


if __name__ == "__main__":
    conn = create_con("cis3368spring.cb0eqkk045ol.us-east-1.rds.amazonaws.com",
                      "angeloangel",
                      "serdon17",
                      "cis3368springdb")

    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM drinks"  # String we want to deliver
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    print("Drinks Menu: ")
    for drink in rows:
        print(f"{drink['id']} - {drink['drinkname'].capitalize()}: ${drink['price']}")
    print()
        
    while True:
        user_choice = input("Start an order or get information about a drink?  \
                    \ns - Start an order \
                    \ng - Get drink information \
                    \nq - Get total\n").lower().strip()
        print()
        
        total = []
        
        if user_choice == "s":
            print(user_choice)
        elif user_choice == "g":
            print(user_choice)
        elif user_choice == "q":
            print(user_choice)
        else:
            print("Invalid choice, try again")
            continue
