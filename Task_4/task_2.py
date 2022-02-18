import random,string
characters = list("!@#$%^&*()~" + string.ascii_lowercase + string.ascii_uppercase + str(random.randint(0,9)))
random.shuffle(characters)
password = []
for x in range(0,8):
    password.append(random.choice(characters))  
password.extend((str(random.randint(0,9)) ,random.choice(['@', '#', '$', '%', '&'])))
random.shuffle(password)
print("password : {}".format("".join(password)))
