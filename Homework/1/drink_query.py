import mysql.connector
from mysql.connector import Error


# Connect to my database
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


# Asks user to enter a valid ID number within a domain, otherwise repeat until satisfied
def get_valid_drink_id():
    while True:
        try:
            drink_id = int(input("Enter the drink ID number associated with the drink: "))
        except ValueError:
            print("Enter a digit only\n")
            continue

        if (drink_id > 0) and (drink_id <= 10):
            return drink_id
        else:
            print("Invalid domain, try again\n")


if __name__ == "__main__":
    conn = create_con("cis3368spring.cb0eqkk045ol.us-east-1.rds.amazonaws.com",
                      "angeloangel",
                      "angelopassword",
                      "cis3368springdb")

    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM drinks"  # String we want to deliver
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    # Runs menu once throughout the program run 
    print("Drinks Menu: ")
    for drink in rows:
        print(f"{drink['id']} - {drink['drinkname'].capitalize()}: ${drink['price']}")
    print()

    total = []
    drinks = []
    # Infinite loop until user finishes ordering and asks for receipt
    while True:
        user_choice = input("Start an order or get information about a drink?  \
                    \ns - Add order \
                    \ng - Get drink information \
                    \nq - Get total\n").lower().strip()
        print()

        # Adds user choices into their corresponding lists
        if user_choice == "s":
            selected_drink_id = get_valid_drink_id()

            for user in rows:
                if user["id"] == int(selected_drink_id):
                    total.append(user['price'])
                    drinks.append(user['drinkname'])
                else:
                    continue
            print()

        # Display drink information according to user choice
        elif user_choice == "g":
            selected_drink_id = get_valid_drink_id()

            # Goes through every row. Only output a particular row that matches user's choice of drink id
            for user in rows:
                if user["id"] == int(selected_drink_id):
                    print("\nDrink information")
                    print(f"Description: {user['descript']}")
                    print(f"Color: {user['color']}")
                else:
                    continue
            print()

        # Receipts the lists of orders the user have
        elif user_choice == "q":
            if len(total) == 0:
                print("You didn't order anything...")
                print("No receipt for you")
            else:
                print(f"{'RECEIPT':^31}")
                print(f"{'Drinks':<15}|{'Price':>15}")
                print(f"{'-'*15}+{'-'*15}")
                for item in range(len(total)):
                    duh = f"${total[item]}"
                    print(f"{drinks[item]:<15}|{duh:>15}")
                sum_total = f"${sum(total):.2f}"
                print("-"*31)
                print(f"Total:{' '*14}{sum_total:>10}")
            break

        # Notifies user of an invalid choice
        else:
            print("Invalid choice, try again")
            print()
            continue
