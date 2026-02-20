n = int(input("Enter numbers of elemments:"))
sum = 0
product = 1

for i in range(1, n+1):
    num = int(input(f"Enter number {i}: "))
    sum += num;
    product *= num;

    average = sum/n;

print("Sum =", sum)
print("Product =", product)
print("Average =", average)

      
    
