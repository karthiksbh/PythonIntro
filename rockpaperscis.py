import random

print("-------------This is a Rock,Paper and Scissors game!!!-------------")
print("Instructions: ")
print("(i)Select any one of rock,paper or scissors")
print("(ii)You will have five chances to win against the computer")
print("(iii)Enter R for rock, S for scissors and P for paper")
print("")

game=['R','P','S']
z=input("Enter the player name: ")
a=0
computer=0

print("-----R:Rock-----S:Scissors-----P:Paper-----")
print("")

print("-------------Let the game begin-------------")
print("----------------Five Chances----------------")
print("")
for i in range(0,5):
    print("")
    x=game[random.randint(0,2)]
    y=input("Select R,S or P: ")
    print("Computer plays: " + x)
    if(y=='R'):
        if(x=='R'):
            print("Tie")
        if(x=='P'):
            print("Computer Wins")
            computer=computer+1
        if(x=='S'):
            print("You Win")
            a=a+1
    elif(y=='S'):
        if(x=='S'):
            print("Tie")
        if(x=='R'):
            print("Computer Wins")
            computer=computer+1
        if(x=='P'):
            print("You Win")
            a=a+1
    elif(y=='P'):
        if(x=="P"):
            print("Tie")
        if(x=='S'):
            print("Computer Wins")
            computer=computer+1
        if(x=='R'):
            print("You Win")
            a=a+1
    else:
        print("Choose suitable input")
print("")
print(str(z) + " score is: " + str(a))
print("Computer Score is: " + str(computer))
print("")

if(a>computer):
    print("Congratulations You Win!!!!!")
    print("")
elif(computer>a):
    print("You Lose. Better luck next time")
    print("")
else:
    print("Tie!!")
    print("")

z=input()