print("* * * * * * * * * * * * * * * * * * * * * * * * * * * \n* * *  Welecome to rock , paper , scissor game  * * * \n* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

import random

attempts= 1
your_point=0
computer_point=0
tie=0
while (attempts<=3):

    lst=["rock","paper","scissor"]
    ran=random.choice(lst)
    print("what do you choose rock, paper or scissor")
    inp=input()

    if inp==ran:
        print("tie")
        tie = tie +1
        print("--------------------------")
        print(f"Computer:{computer_point}, You:{your_point}, Tie:{tie}")
        print("--------------------------")

    elif inp=="rock" and ran=="paper":
        print("Paper wraps the rock\n")
        computer_point = computer_point +1
        print("You LOST")
        print("--------------------------")
        print(f"Computer:{computer_point}, You:{your_point}, Tie:{tie}")
        print("--------------------------")

    elif inp=="paper" and ran=="rock":
        # print(f"you choosed {inp} and computer guess is {ran}")
        your_point = your_point + 1
        print("The paper wraps the rock\n")
        print("You WON")
        print("--------------------------")
        print(f"Computer:{computer_point}, You:{your_point}, Tie:{tie}")
        print("--------------------------")

    elif inp=="paper" and ran=="scissor":
        # print(f"you choosed {inp} and computer guess is {ran}")
        computer_point = computer_point + 1
        print("The scissor cuts the paper\n")
        print("You LOST")
        print("--------------------------")
        print(f"Computer:{computer_point}, You:{your_point}, Tie:{tie}")
        print("--------------------------")

    elif inp == "scissor" and ran == "paper":
        # print(f"you choosed {inp} and computer guess is {ran}")
        your_point = your_point + 1
        print("The scissor cuts the paper\n")
        print("You WON")
        print("--------------------------")
        print(f"Computer:{computer_point}, You:{your_point}, Tie:{tie}")
        print("--------------------------")

    elif inp == "scissor" and ran == "rock":
        # print(f"you choosed {inp} and computer guess is {ran}")
        computer_point = computer_point + 1
        print("The rock breaks the scissor\n")
        print("You LOST")
        print("--------------------------")
        print(f"Computer:{computer_point}, You:{your_point}, Tie:{tie}")
        print("--------------------------")

    elif inp == "rock" and ran == "scissor":
        # print(f"you choosed {inp} and computer guess is {ran}")
        your_point = your_point + 1
        print("The rock breaks the scissor\n")
        print("You WON")
        print("--------------------------")
        print(f"Computer:{computer_point}, You:{your_point}, Tie:{tie}")
        print("--------------------------")

    else:
        print("invalid")

    print(10 - attempts, "no. of guesses left")
    attempts = attempts + 1

    if attempts>10:
        print("Game Over")

print(f"FINAL SCORE: Your have scored {your_point} points and the Computer scored {computer_point} points")

if computer_point > your_point:
    print("Computer beat you")

if computer_point < your_point:
    print("Congratulations, You've beaten the Computer")

