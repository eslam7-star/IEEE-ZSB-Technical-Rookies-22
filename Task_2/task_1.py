n = int(input("Enter the number n : ")) 
result = "prime numbers to {} are :".format(n)
for i in range(2, n+1): 
    count = 0  
    for j in range(1, i+1): 
        if i % j == 0: 
            count += 1  
    if count < 3: 
        result += " {} ".format(i)
print(result)
