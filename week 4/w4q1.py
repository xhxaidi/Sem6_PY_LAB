def calculate_average(marks):
    return sum(marks) / 5

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def rectangle_perimeter(length, width):
    return 2 * (length + width)

print("Average =", calculate_average([-10, 0, 20, 30, 40]))
print("Temperature =", celsius_to_fahrenheit(36.5), "°F")
print("Perimeter =", rectangle_perimeter(10, 5))

