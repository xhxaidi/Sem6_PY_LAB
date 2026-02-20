import math

# Function to calculate effective area of circular flower bed
def effective_area(R, r):
    if R <= r:
        return "Invalid input"
    return math.pi * (R**2 - r**2)


R1 = float(input("Enter the outer radious :"))
r1 =float(input("Enter the inner radious :"))
area1 = effective_area(R1, r1)
print("Effective Area =", round(area1, 2))


