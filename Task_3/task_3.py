def searcher(arr,val):
    init_index = 0
    fin_index = len(arr) - 1
    while(init_index <= fin_index):
        init_mid = (init_index + fin_index) // 2
        if arr[init_mid] == val :
            return init_mid
        elif arr[init_mid] < val :
            init_index = init_mid +1
        else:
            fin_index = init_mid -1
print(searcher([1,2,3,4,5,6,7,8,9,10],7))



