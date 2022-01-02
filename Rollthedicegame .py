import random
while True:
    game = input("would you like to roll the dice? Y/N")
    if game == "Y":
        User = random.randint(1,6)
        print ("you rolled a", User, "!")
        Comp = random.randint(1,6)
        print ("The computer rolled a", Comp, "!")
        if User > Comp:
            print ("you win!")
        elif User < Comp:
                print ("you lose")
        if User == Comp:
            print ("its a draw")
    if game == "N":
        print ("Thank you for playing. Have a great day!")
        break
    else:
        print ("Sorry, please say 'Y' or 'N'")
         








