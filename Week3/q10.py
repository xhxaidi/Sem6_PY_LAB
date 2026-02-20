n = int(input("Enter a number: "))
a, b= 0, 1
isfibo = False

while a<=n:
    if a ==n:
        isfibo = True
        break
    a, b = b, a+b

if isfibo:
    print("Fibonacci Number")
else:
    print("Not a fibonacci number")
    
