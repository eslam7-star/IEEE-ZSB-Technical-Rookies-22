n =int(input("enter your n bottles : ").strip())
my_dict ={}
for i in range(0,n):
    volume , cap = input("enter each bottle voulme and capacity separated by a space : ").strip().split() 
    my_dict[int(volume.strip())] = int(cap.strip())
itms = my_dict.keys()
sm = sum(itms)
ls = list(my_dict.values())
max1 = max(ls)
ls.remove(max1)    
if max1 + max(ls) >= sm :
    print("Yes")
else:
    print("No")      