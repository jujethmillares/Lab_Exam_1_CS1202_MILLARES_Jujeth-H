# Lab Exam 1 // CS 1202
# MILLARES, Jujeth H.

#This dictionary contain the games in the game rental system.
game_library = {
    1: {"Donkey Kong": {"copies_available": 3, "cost": 2}},
    2: {"Super Mario Bros": {"copies_available": 5, "cost": 3}},
    3: {"Tetris": {"copies_available": 2, "cost": 1}},
    4: {"The Adventure Pals": {"copies_available": 5, "cost": 4}},
    5: {"Castlevania": {"copies_available": 7, "cost": 5}}
}

#This is the user account
user_accounts = {}

# Function to display all games in the system along with their availability, quantity, and cost.
def display_available_games():
    print("\nGame Library:")
    for game_id, game_info in game_library.items():
        print(f"ID: {game_id}")
        for game_title, game_details in game_info.items():
            print(f"  Title: {game_title}")
            print(f"  Copies Available: {game_details['copies_available']}")
            print(f"  Cost: ${game_details['cost']}")
            print()
    main()  # Returning to the main main after displaying games

# Function to register a new user account.
def register_user():
    while True:
        print("Register as new user ")
        print("Please provide the following details")
        username = input("\nPlease input username: ")
        password = input("Please input password(must be 8 characters long): ")
        if len(password) >= 8:
            print("\nACCOUNT REGISTERED SUCCESSFULLY..........\n")
            user_balance = 0
            user_points = 0

            # Creating a new user account and the collected data will be stored to the user_accounts
            user_accounts[username] = {
                "username": username,
                "password": password,
                "Balance": user_balance,
                "Points": user_points
            }
            main()  # Returning to the main main after successfully register_usering
        else:
            print("\nPassword must be at least 8 characters long")
            continue
        return

# Function to rent a game after the user successfully logs in.
def rent_game(username):
    while True:
        game_id = input("\nPlease enter game ID: ")
        # Checking if the entered game ID is a valid integer and exists in the game library
        if game_id.isdigit() and int(game_id) in game_library:
            game_id = int(game_id)
            game_title, game_details = next(iter(game_library[game_id].items()))
            copies_available = game_details["copies_available"]
            cost = game_details["cost"]

            # If the game is available in stock
            if copies_available > 0:
                # If the user has enough balance to rent the game
                if user_accounts[username]["Balance"] >= cost:
                    user_accounts[username]["Balance"] -= cost
                    game_details["copies_available"] -= 1
                    print(f"\nSuccessfully rented '{game_title}'\n")

                    # Calculating points earned for renting the game
                    points_earned = cost // 2  
                    user_accounts[username]["Points"] += points_earned
                    print(f"\nYou earned {points_earned} point(s) for renting '{game_title}'.")
                else:
                    print("\nInsufficient balance to rent the game.\n")
            else:
                print(f"\n'{game_title}' is currently out of stock.\n")
            break
        else:
            print("\nInvalid game ID. Please enter a valid game ID.\n")

#This function will let the user return the game and also update the copies available in the game library.
def return_game(username):
    print()
    print(f"Logged in as {username}")
    print("Return a game")
    game_name = input("\nEnter the name of the game you want to return: \n")

    # Use a list comprehension to iterate over games in the library
    game_found = next((game_id for game_id, game_info in game_library.items() if game_name in game_info), None)

    if game_found:
        game_details = game_library[game_found][game_name]
        game_details["copies_available"] += 1
        print(f"\n{game_name} returned successfully.\n")
    else:
        print("\nSorry, the game you entered is not available for return.\n")

# Function to top up the user's account balance with a chosen amount.
def top_up_account(username):
    print(f"Logged in as {username}")
    print(f"Top Up")
    amount = float(input("\nEnter the amount you want to top up: \n"))
    # Checking if the entered amount is positive
    if amount > 0:
        user_accounts[username]["Balance"] += amount
        print(f"\nTopping up, please wait...........\n")
        print(f"\nTop-up successful. Current balance: ${user_accounts[username]['Balance']}\n")
    else:
        print("\nInvalid amount. Please enter a positive value.\n")

# Function to display the user's display_inventory, showing the number of copies rented for each game.
def display_inventory(username):
    print()
    print(f"Logged in as {username}")
    print("INVENTORY:")
    for game_id, game_info in game_library.items():
        for game_name, details in game_info.items():
            copies_rented = details["copies_available"]
            # Checking if any copies of the game are rented
            if copies_rented < 3:
                print(f"{game_name}: {3 - copies_rented} copies rented")
            else:
                print(f"{game_name}: No copies rented")


# Function to update the quantity of a game in the game library.
def update_game_quantity():
    print("\nUPDATE GAME QUANTITY")
    game_id = input("Enter the game ID: ")
    # Checking if the entered game ID is valid and exists in the game library
    if game_id.isdigit() and int(game_id) in game_library:
        game_id = int(game_id)
        game_title = list(game_library[game_id].keys())[0]
        new_quantity = int(input("Enter the new quantity: "))
        # Updating the quantity of the game
        game_library[game_id][game_title]["copies_available"] = new_quantity
        print("\nQuantity updated successfully.\n")
    else:
        print("\nInvalid game ID.\n")


# Function to update the cost of a game in the game library.
def update_game_cost():
    print("\nUPDATE GAME COST")
    game_id = input("Enter the game ID: ")
    # Checking if the entered game ID is valid and exists in the game library
    if game_id.isdigit() and int(game_id) in game_library:
        game_id = int(game_id)
        game_title = list(game_library[game_id].keys())[0]
        new_cost = float(input("Enter the new cost: "))
        # Updating the cost of the game
        game_library[game_id][game_title]["cost"] = new_cost
        print("\nCost updated successfully.\n")
    else:
        print("\nInvalid game ID.\n")


# Function for admin login.
def admin_login():
    admin_credentials = {"admin": "adminpass"}

    while True:
        print("ADMIN LOGIN PAGE")
        admin = input("Please enter username: ")

        if admin in admin_credentials:
            admin_pass = input("Please enter password: ")
            if admin_pass == admin_credentials[admin]:
                print("\nLogin Successful\n")
                admin_main()
                return
            else:
                print("\nIncorrect password\n")
        else:
            print("\nIncorrect Username\n")

# Function for the admin main.
def admin_main():
    while True:
        print("\nADMIN main")
        print("1. Update game quantity")
        print("2. Update game cost")
        print("3. Logout")

        choice = input("Enter your choice: ")

        # Redirecting to the corresponding function based on admin choice
        if choice == "1":
            update_game_quantity()
        elif choice == "2":
            update_game_cost()
        elif choice == "3":
            print("Logging out...Goodbye!")
            main()  # Returning to the main main after logging out
        else:
            print("\nPlease enter a valid choice.\n")

# Function to redeem a free game if the user has enough points.
def redeem(username):
    points_for_free_game = 3

    # Check if the user has enough points to redeem a free game
    if user_accounts[username]["Points"] >= points_for_free_game:
        # Update the user's points balance
        user_accounts[username]["Points"] -= points_for_free_game
        print("\nCongratulations! You've earned 1 free game.\n")
    else:
        print("\nSorry, you don't have enough points to redeem a free game.\n")

# Function to display the user main after logging in.
def user_main(username):
    while True:
        print(f"\nLogged in as {username}")
        print("1. Rent a game")
        print("2. Return a game")
        print("3. Top-up Account")
        print("4. Display display_inventory")
        print("5. Redeem free game rental")
        print("6. Check Points")
        print("7. Log out")

        choice = input("Enter your choice: ")

        # Redirecting to the corresponding function based on user choice
        if choice == "1":
            rent_game(username)
        elif choice == "2":
            return_game(username)
        elif choice == "3":
            top_up_account(username)
        elif choice == "4":
            display_inventory(username)
        elif choice == "5":
            redeem(username)
        elif choice == "6":
            check_point(username)
        elif choice == "7":
            print("Logging out...Goodbye!")
            main()  # Returning to the main main after logging out
            break
        else:
            print("\nPlease input 1-7 only\n")

# Function to log in an existing user account.
def check_credentials():
    while True:
        print("Login existing user account")
        username = input("\nPlease enter username: ")
        password = input("Please enter password: ")
        if username in user_accounts and user_accounts[username]["password"] == password:
            print("\nLOGIN SUCCESSFUL........\n")
            user_main(username)  # Redirecting to the user main after successful login
            break
        else:
            print("\nInvalid username or password")


# Function to display the main main of the game rental system
def main():
    while True:
        # Displaying the main options
        print("*" * 35) 
        print("* Welcome to the Game Rental System *")
        print("*" * 35)
        print("1. Display Available Games")
        print("2. register_user User")
        print("3. Log in")
        print("4. Admin Log in")
        print("5. Exit")

        # Asking user for their input or choice
        choice = input("\nEnter your choice: ")

        # Determining the user's choice and directing them to the corresponding function
        if choice == "1":
            print()                
            display_available_games()
        elif choice == "2":
            print()
            register_user()
        elif choice == "3":
            check_credentials()
        elif choice == "4":
            admin_login()
        elif choice == "5":
            print("Closing system...Goodbye!")
            return
        else:
            print("\nPlease input a valid option\n")
            main()  # Directing back to main()  if the user input an invalid option 
    return


# Function to display the user's points balance.
def check_point(username):
    print(f"Logged in as {username}")
    points = user_accounts[username]["Points"]
    print(f"\nYou have {points} points.\n")             

if __name__ == "__main__":
    main()