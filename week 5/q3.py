s = input("enter the string:")

# removing noisy(special) character at odd place ->
step1= ""
for i in range(len(s)):
    if i%2!=0 and not s[i].isalnum():
        continue
    step1 +=s[i]

#removing the char at even place-> 
final=""
for i in range(len(step1)):
    if i%2!=0:
        final+=step1[i]
        
print(final)

