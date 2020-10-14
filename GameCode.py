#Snake Water and Gun Game

import random

def gameWin(comp,you):
    #If two values are equal, it will declare a tie
    if comp==you:
        return None
    #Checking for all possibilities when computer choses s
    elif comp== 's':
        if you== 'w':
            return False
        elif you== 'g':
            return True

    #Checking for all possibilities when computer choses w
    elif comp== 'w':
        if you== 'g':
            return False
        elif you== 's':
            return True
    #Checking for all Possibilities when computer choses g
    elif comp== 'g':
        if you== 's':
            return False
        elif you== 'w':
            return True


print("Computer's turn: Snake(s), Water(w) or Gun(g)?")
randNo= random.randint(1,3)

if randNo== 1:
    comp = 's'
elif randNo== 2:
    comp= 'w'
elif randNo== 3:
    comp= 'g'


you = input("Your turn: Snake(s), Water(w) or Gun(g)?\n")
a= gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You Chose {you}")

if a== None:
    print("A game is tied!")
elif a:
    print("Hurray! You Won!")
else:
    print("Ooops! You Lose!")

   
