n = int(input("enter the number of numbers in your list :"))
ls = ""
diffe = []
for x in range(0,n):
    x = int(input("enter your number : "))
    ls += str(x)
for x in ls:
    if ls.rfind(x) != ls.find(x):
        diffe.append(ls.rfind(x)-ls.find(x))
print("the minimum distance between two similar numbers is :", min(diffe))        

         



