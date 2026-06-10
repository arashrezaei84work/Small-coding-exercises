
# (Just a test for match-case)

try:
    day = int(input("Enter a day : "))
    month = int(input("Enter a month : "))
    year = int(input("Enter a year : "))


    def calender(day, month, year):
        birthday = 0
        match birthday:
            case a if 1 > month > 12 and day > 31:
                print("Invalid month")
            case a if month > 10:
                birthday = year + 622
            case a if month == 10 and day > 10:
                birthday = year + 622
            case _:
                birthday = year + 621
        print(f"your birthday is {birthday}")


    calender(day, month, year)
except ValueError:
    pass
