from os import system
from random import choice

rand = choice(list(range(1, 11)))

if rand == 1:
    system("bash ~/.ran/1.sh")
elif rand == 2:
    system("bash ~/.ran/2.sh")
elif rand == 3:
    system("bash ~/.ran/3.sh")
elif rand == 4:
    system("bash ~/.ran/4.sh")
elif rand == 5:
    system("bash ~/.ran/5.sh")
elif rand == 6:
    system("bash ~/.ran/6.sh")
elif rand == 7:
    system("bash ~/.ran/7.sh")
elif rand == 8:
    system("bash ~/.ran/8.sh")
elif rand == 9:
    system("bash ~/.ran/9.sh")
elif rand == 10:
    system("bash ~/.ran/10.sh")
else:
    print("FUCK, THERES AN ERROR")
