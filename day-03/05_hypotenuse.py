import math

side_a = float(input("Enter the length of side a in metres: "))
side_b = float(input("Enter the length of side a in metres: "))

if side_a <= 0 or side_b <= 0:
    print("Error: Side must be greather than zero.")
else:
    hypotenuse = math.sqrt(side_a**2 + side_b**2)
    print("The hypotenuse is",round(hypotenuse, 2), "metres")