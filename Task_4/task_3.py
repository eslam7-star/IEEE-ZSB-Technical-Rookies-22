def sort_algorithm(ls):
    for i in range(1,len(ls)):
        while ls[i] < ls[i-1] and i>0:
            ls[i] , ls[i-1] = ls[i-1] , ls[i]
            i = i-1
    return ls
print(sort_algorithm([2,5,7,9,1,0,4,6,7,2]))