from math import pi as p


# =====================================
def cylinder_area():
    r = float(input("Enter the radius: "))
    h = float(input("Enter the height: "))

    def AreaOfCircle():
        x = r * r * p
        return x

    def AreaOfRectangle():
        y = (r * p * 2) * h
        return y

    def Result():
        result = (AreaOfCircle() * 2) + AreaOfRectangle()
        return result

    return Result()


Final_Result = cylinder_area()

print(f"The final result is {Final_Result:.2f}")
