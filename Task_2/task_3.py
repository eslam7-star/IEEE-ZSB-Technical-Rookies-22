sentence = input("Enter your sentence : ")
words = sentence.strip().split(' ')
new_words = []
max_word_lenght = len(max(words, key=len)) 
for x in words:
    if (x +"1") != "1":  
        y = "* "+ x.strip() + " "*(max_word_lenght - len(x)) + " *"
        new_words.append(y)
frame_bar = '*'*(max_word_lenght+4)
for i in new_words:
    frame_bar += '\n'+ i
print(frame_bar + '\n' +'*'*(max_word_lenght+4))    