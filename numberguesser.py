import random

print("--------------------------Random Number Guesser--------------------------")
print("")
print("Instructions for the game: ")
print("(i)This is a number guessing game. You have to enter the upper and lower boundary condition first")
print("(ii)The compiler will generate a number in between the upper and lower boundary conditions(both included)")
print("(iii)You have 7 chances to guess the number")
print("")
a=int(input("Enter the lower boundary condition: "))
c=0
b=int(input("Enter the upper boundary condition: "))
x=random.randint(a,b)
print("")
print("------------------You have total seven attempts to guess------------------")
print("")
for i in range(0,7):
    y = int(input("Select a number in range: "))
    if(x==y):
        c=1
        print("Congratulations you have guessed the number in " + str(i+1) + " try")
        break
    elif(y>x):
        print("You have guessed a number higher than required!!!!!")
        print("")
    elif(y<x):
        print("You have guessed a number lower than required!!!!!")
        print("")
if(c==0):
    print("Better luck next time!!!")

a=input()