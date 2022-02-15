x = int(input("Enter number os items in your list :"))
ls = []
for i in range (0,x):
    ls.append(int(input("enter your number :")))  
ls.sort()    
sls = set(ls)  
print(sls)

