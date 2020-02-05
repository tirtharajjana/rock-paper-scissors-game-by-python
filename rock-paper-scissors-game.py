import random
print("WELCOME TO ROCK-PAPER-SCISSORS GAME")
print()

game=int(input("How many game you want to play "))
i=0
c=0
m=0
t=0
while i<game:
    lst=["r","p","s"]
    c_turn=random.choice(lst)
    you=input("your turn plz press 'r' for Rock,'p' for paper,'s' for scissors ")
    if (c_turn=='r' and you=='r') or (c_turn=='p' and you=='p') or (c_turn=='s' and you=='s'):
        print("Tie ")
        t=t+1
    elif (c_turn=='p' and you=='s') or (c_turn=='r' and you=='p') or (c_turn=='s' and you=='r'):
        print(" Win")
        m=m+1
    elif (c_turn=='s' and you=='p') or (c_turn=='r' and you=='s') or (c_turn=='p' and you=='r'):
        print("Lose")
        c=c+1

    else:
        print("Plz enter a valid Key")
        i=i-1    

    i=i+1


print("u win ",m,"time")

print("computure win ",c,"time")

print("tie" ,t,"time")