import random

rnd_num = random.randint(1,10)
nums_trials = 1
while(True):
    x = int(input("guess a number : "))
    if rnd_num == x :        
        print("you got it {} trials".format(nums_trials))
        break
    nums_trials +=1
    print("Wrong guess ")    


