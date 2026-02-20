# Function to calculate sum of digits
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

n = int(input("Enter the number:"))
result = sum_of_digits(n)
print("Sum of digits =", result)

