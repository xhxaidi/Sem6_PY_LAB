number =int(input("Enter the number : "))
Tsum = 0 
for i in range(1,number):
    if number%i==0:
        Tsum+=i

if Tsum ==number:
    print(number,"is the perfect number")
else:
    print(number, "is not the perfect number")
    
    