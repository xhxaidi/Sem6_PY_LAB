import math

# Function to calculate volume of a sphere
def volume_of_sphere(radius):
    if radius < 0:
        return "Invalid radius"
    return (4/3) * math.pi * radius**3

radius1 =float(input("Enter the radious :"))
result1 = volume_of_sphere(radius1)
print("Volume =", round(result1, 3), "cm³")


