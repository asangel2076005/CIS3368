def print_menu():
    print("MENU \n" 
          "a - Add player \n"
          "d - Remove player \n"
          "u - Update player rating \n"
          "r - Output players above a rating \n"
          "o - Output roster \n"
          "q - Quit")


if __name__ == "__main__":
    soccer_team_dict = {
        "jersey_number": {},
        "ratings": {}
    }

    for i in range(5):
        name = input("Enter player's name: ")
        soccer_team_dict["jersey_number"][f"{name.lower().strip()}"] = \
            int(input(f"Enter {name.strip()}'s jersey number: "))

        soccer_team_dict["ratings"][f"{name.lower().strip()}"] = \
            int(input(f"Enter {name.strip()}'s ratings: "))
    print()

    print_menu()
    print()
    while True:
        user_choice = input()
        print()

        if user_choice == "a":
            name = input("Enter new player's name: ").lower().strip()
            soccer_team_dict["jersey_number"][f"{name.lower()}"] = \
                int(input(f"Enter {name.capitalize()}'s jersey number: "))

            soccer_team_dict["ratings"][f"{name.lower()}"] = \
                int(input(f"Enter {name.capitalize()}'s ratings: "))
            print()

        elif user_choice == "d":
            name = input("Enter the player's name to be removed from the data: ").lower().strip()
            del soccer_team_dict["jersey_number"][name]
            del soccer_team_dict["ratings"][name]
            print()

        elif user_choice == "u":
            name = input("Enter the player's name to update their ratings: ").lower().strip()
            rating = int(input("Enter rating: "))
            soccer_team_dict["ratings"][name] = rating
            print()

        elif user_choice == "r":
            threshold = int(input("Enter minimum rating: "))
            print()

            print("Ratings: ")
            for key, value in soccer_team_dict["ratings"].items():
                if value > threshold:
                    print(f"    {key.capitalize()}: {value}")
            print()

        elif user_choice == "o":
            name_list = [keys for keys in soccer_team_dict["jersey_number"].keys()]
            jersey_num_list = [values for values in soccer_team_dict["jersey_number"].values()]
            ratings_list = [values for values in soccer_team_dict["ratings"].values()]

            for i in range(len(name_list)):
                print(f"{name_list[i].capitalize()}'s jersey number is {jersey_num_list[i]} "
                      f"and rating is {ratings_list[i]}")
            print()

        elif user_choice == "q":
            break
