from utils.user_manager import UserManager
from utils.dice_game import DiceGame

def menu():
    print("1. Start game")
    print("2. Show top scores")
    print("3. Log out")

def login(user_manager):
    print("Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if user_manager.validate_login(username, password):
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None
def register(user_manager):
    print("Registration")
    username = input("Enter username (min 4 chars): ")
    password = input("Enter password (min 8 chars): ")
    if len(username) < 4 or len(password) < 8:
        print("Invalid username or password. Username must be at least 4 characters and password must be at least 8 characters.")
        return
    if user_manager.validate_username(username):
        print("Username already exists. Please choose another one.")
        return
    user_manager.register(username, password)
    print("Registration successful.")

if __name__ == "__main__":
    user_manager = UserManager()
    user_manager.load_users()
    while True:
        print("Welcome to the dice roll game")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice, or leave blank to cancel: ")
        if choice == "1":
            register(user_manager)
        elif choice == "2":
            username = login(user_manager)
            if username:
                while True:
                    menu()
                    choice = input("Enter your choice, or leave blank to cancel: ")
                    if choice == "1":
                        dice_game = DiceGame(user_manager)
                        dice_game.current_user = username
                        dice_game.play_game()
                    elif choice == "2":
                        dice_game = DiceGame(user_manager)
                        dice_game.show_top_scores()
                        print("\n")
                    elif choice == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice.")
