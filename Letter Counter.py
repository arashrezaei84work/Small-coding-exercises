
# (Just a test for match-case)
def counter_letter(name=''):
    low = 0
    ups = 0
    for n in name:
        match name:
            case a if n.islower():
                print(f"lowercase : {n}")
                low += 1
            case a if n.isupper():
                print(f"uppercase : {n}")
                ups += 1
            case a if n.isdigit():
                print("string not found")
            case _:
                print("Invalid character")
    print(f"Lower count : {low}\nUpper count : {ups}")


while True:
    name = input("Enter your name : ")
    if name == 'close' or name == 'exit':
        break
    counter_letter(name)
