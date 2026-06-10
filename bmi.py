
"""
This Program can calculate the bmi of a person(Just a test for match-case)
"""

height = float(input("Enter your height (cm) : "))
weight = float(input("Enter your weight (kg) : "))

bmi = weight / ((height / 100) ** 2)
print(" -----------------")
match bmi:
    case x if x <= 18.5:
        print(" you are underweight")
    case x if 18 < x <= 25:
        print(" You are normal")
    case x if 25 < x <= 30:
        print(" you are overweight")
    case x if 30 < x:
        print(" you are obese(class 1)!")
    case x if 40 < x:
        print(" you are obese(class 2)!!!")
    case _:
        print(" something were wrong!")

print(f"\n your bmi is {bmi:.2f}")

