import random
import pyttsx3
import time
a=int(input("press 1 for start:"))
p=0
list=[]
engine = pyttsx3.init()
if (a==1):
    print("--------------GAME STARTS------------------------ ")
    while len(list)!=90:
        num = random.randrange(1,91)
        if num not in list:
            list.insert(p,num)
            engine.say(num)
            engine.runAndWait()
            print(num)
            time.sleep(3)  
            p+=1  
        
else:
    print("WRONG INPUT ")
print("---------------------------------------------------------------------")
print(list)

