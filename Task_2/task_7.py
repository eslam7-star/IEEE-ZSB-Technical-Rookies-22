x = input()
ls = input().strip().split(' ')
c = False
for i in ls:
    if int(i) > 0: 
        if int((i)[::-1]) == int(i):  
            c = True  
    else:
        c = False
        break    
print(c)       
       
        
    
   