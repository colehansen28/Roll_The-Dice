import random
User_Score = 0
Comp_Score = 0
while True:
    game = input("would you like to roll the dice? Y/N")
    if game == "Y":
        User = random.randint(1,6)
        print ("you rolled a", User, "!")
        Comp = random.randint(1,6)
        print ("The computer rolled a", Comp, "!")
        if User > Comp:
            print ("you win!")
            User_Score+=1
        elif User < Comp:
            print ("you lose")
            Comp_Score+=1
        if User == Comp:
            print ("its a draw")
        print("Player Score:", User_Score)
        print("Oppenent Score:", Comp_Score)
    if game == "N":
        print ("Thank you for playing. Have a great day!")
        break
    else:
        print ("Sorry, please say 'Y' or 'N'")
         








