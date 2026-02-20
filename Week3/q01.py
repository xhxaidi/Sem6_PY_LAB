n= int(input("Enter the number of price: "))
prices=[]
product =1 
total_sum =0
 
for i in range(n):
    price = int(input("enter the price: "))
    prices.append(price)
    
    total_sum +=price
    
    
    for p in prices:
        product*=p
        
        average =total_sum/n
        
    print("sum: ", total_sum);
    print("product: ",product)
    print ("average: ", average)
    
 