import random
h1=100
h2=100
def show_heal():
    print("your heal is : ",h1)
    print("bot heal is : ",h2)

def damage_user():
    global h1
    h1=max(0,h1-10)
def damage_bot():
    global h2
    h2=max(0,h2-10)
def heal_user():
    global h1
    h1=min(100,h1+10)
def heal_bot():
    global h2
    h2=min(100,h2+10)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("    **WELCOME TO THE ARENA** ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print ("(1) for heal user  (2) for damage bot (3) for damage user (4) for heal bot")

while True:
    x=(random.randint(3 ,4))
    print("bot chose : ",x)
    y=int(input("please enter a number between 1 to 4 : "))
    
    if y==1:
        heal_user()
    elif y==2:
        damage_bot()
    elif y==3:
        damage_user()
    elif y==4:
        heal_bot()
    else:
        print("invalid input")
    show_heal()
    if h1==0 or h2==0:
        if h1==0:
            print("bot win")
        else:
            print("you win")
        break

