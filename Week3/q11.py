n = int(input("Enter a number: "))

if n<= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n%i == 0:
            print("Not prime, first factor:", i)
            break
    
    print("Prime number")  
            
            
