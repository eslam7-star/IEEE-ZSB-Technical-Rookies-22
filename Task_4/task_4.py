seq1 = input("enter your sequence of letters : ")
n = int(input("enter n : "))
compl_seq =[]
counter = 0
for i in range(0,n):
    if counter > len(seq1)-1:
        counter = 0
    compl_seq += seq1[counter]
    counter+=1    
print("number of repeation of r in {} : {}".format("".join(compl_seq),compl_seq.count('r')))