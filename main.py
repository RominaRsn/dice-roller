import random

def roll():
    
    x=random.randint(1,6)
    print(x)
    return x

roll()
print("would u like to roll again?! [y/n]")
k=input()

while(k =="y"):

    roll()
    print("would u like to roll again?! [y/n]")
    k=input()
