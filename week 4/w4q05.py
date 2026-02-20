def sum_of_digit(num):
    temp = num
    Tsum = 0
    while temp != 0:
        digit = temp % 10
        Tsum = Tsum + digit
        temp //= 10
    return Tsum


n = int(input("Enter the integer: "))
result = sum_of_digit(n)
print("Sum of digits:", result)
