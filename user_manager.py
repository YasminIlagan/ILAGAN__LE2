import os

class UserManager:
    def __init__(self):
        self.users = {}
    
    def load_users(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/users.txt"):
            with open("data/users.txt", "w"):
                pass
        with open("data/users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                self.users[username] = password
    
    def save_users(self):
        with open("data/users.txt", "w") as file:
            for username, password in self.users.items():
                file.write(f"{username},{password}\n")
    
    def register(self, username, password):
        self.users[username] = password
        self.save_users()
    
    def validate_username(self, username):
        return username in self.users
    
    def validate_login(self, username, password):
        return username in self.users and self.users[username] == password
