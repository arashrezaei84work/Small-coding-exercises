class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username} ({self.email})"


class UserManager:
    def __init__(self):
        self.__users = {}

    def add_user(self, username, email):
        if username in self.__users:
            raise ValueError("Username is already registered.")

        new_user = User(username, email)
        self.__users[username] = new_user
        print(f"{username} has registered.")
        return new_user

    def remove_user(self, username):
        if username in self.__users:
            del self.__users[username]
        else:
            raise KeyError("Username is not registered.")

    def find_user(self, username):
        if username in self.__users:
            find = self.__users.get(username)
            return find
        else:
            raise KeyError(f"{username} not found!")

    def list_users(self):
        return self.__users.keys()


user = UserManager()
while True:
    action = input("What would you like to do? ")
    if action == "add":
        user_input, email_input = input("Enter a username: "), input("Enter an email: ")
        try:
            user.add_user(user_input, email_input)
        except ValueError:
            raise "Invalid input."
    elif action == "delete":
        user_input = input("Enter a username: ")
        user.remove_user(user_input)
    elif action == "show":
        print(user.list_users())
    elif action == "find":
        user_input = input("Enter a username: ")
        print(user.find_user(user_input))
    elif action == "exit":
        break
    else:
        print("Invalid input.")
        continue
