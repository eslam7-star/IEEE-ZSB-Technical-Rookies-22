x = int(input("Enter your number greater than one : "))
sum = 0
for i in range(x+1):
    if i % 3 == 0 or i % 5 == 0:     
        sum += i

print("result : {}".format(sum))    
