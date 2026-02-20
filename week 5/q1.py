import math
# 1. Largest of three numbers (positional arguments)
def largest_of_three(a, b, c):
    return max(a, b, c)
# 2. Volume calculations
def volume_cylinder(r, h):
    return math.pi * r * r * h
def volume_cube(a):
    return a ** 3
def volume_rectangular_box(l, w, h):
    return l * w * h
# 3. Area of rectangle
def area_rectangle(l, w):
    return l * w
# 4. Circumference of circle
def circumference_circle(r):
    return 2 * math.pi * r
# 5. Exchange values
def swap_values(a, b):
    return b, a
# 6. Distance between two points
def distance_between_points(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))

print("""
Choose an operation:
1. Largest of three numbers
2. Volume of a shape
3. Area of a rectangle
4. Circumference of a circle
5. Swap two values
6. Distance between two points
""")

choice = int(input("Enter your choice: "))
match choice:
    case 1:
        a, b, c = map(int, input("Enter three numbers: ").split())
        print("Largest =", largest_of_three(a, b, c))

    case 2:
        print("Choose shape: 1-Cylinder  2-Cube  3-Rectangular Box")
        shape = int(input("Enter shape choice: "))

        match shape:
            case 1:
                r, h = map(float, input("Enter radius and height: ").split())
                print("Volume =", volume_cylinder(r, h))
            case 2:
                a = float(input("Enter side: "))
                print("Volume =", volume_cube(a))
            case 3:
                l, w, h = map(float, input("Enter length width height: ").split())
                print("Volume =", volume_rectangular_box(l, w, h))
            case _:
                print("Invalid shape choice")

    case 3:
        l, w = map(float, input("Enter length and width: ").split())
        print("Area =", area_rectangle(l, w))

    case 4:
        r = float(input("Enter radius: "))
        print("Circumference =", circumference_circle(r))

    case 5:
        a, b = input("Enter two values: ").split()
        a, b = swap_values(a, b)
        print("After swap:", a, b)

    case 6:
        x1, y1 = map(float, input("Enter x1 y1: ").split())
        x2, y2 = map(float, input("Enter x2 y2: ").split())
        print("Distance =", distance_between_points(x1, y1, x2, y2))

    case _:
        print("Invalid choice")