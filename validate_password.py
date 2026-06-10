
# (Just a test for match-case)
def validate_pas(pas):
    match pas:
        case x if len(x) < 8:
            print("password must be at least 8 characters")
        case x if x.isnumeric():
            print("password must has at least one letter")
        case x if x.isalpha():
            print("password must has at least one number")
        case x if x.islower():
            print("password must has at least one capital letter")
        case _:
            print("Saved successfully!")


while True:
    password = input("Enter your password : ")
    if password == "close" or password == "exit":
        break
    validate_pas(password)
