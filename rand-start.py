from os import system
from random import choice

rand = choice(list(range(1, 11)))

if rand == 1:
    system("sh ~/.ran/1.sh")
elif rand == 2:
    system("sh ~/.ran/2.sh")
elif rand == 3:
    system("sh ~/.ran/3.sh")
elif rand == 4:
    system("sh ~/.ran/4.sh")
elif rand == 5:
    system("sh ~/.ran/5.sh")
elif rand == 6:
    system("sh ~/.ran/6.sh")
elif rand == 7:
    system("sh ~/.ran/7.sh")
elif rand == 8:
    system("sh ~/.ran/8.sh")
elif rand == 9:
    system("sh ~/.ran/9.sh")
elif rand == 10:
    system("sh ~/.ran/10.sh")
else:
    print("FUCK, THERES AN ERROR")
