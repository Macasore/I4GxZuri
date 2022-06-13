import random

user_win = 0
comp_win = 0
while True:
    options = ["R", "P", "S"]   
    rand = random.randint(0,2)
    computer_input = options[rand]
    user_input = input("Pick an option between R,P or S or Q to quit:  ")
    if user_input == "Q":
        break

    if user_input not in options:
        print("Error no option like that, try again")
        continue

    print('Player(' +user_input+ ') : CPU(' +computer_input+')')
    if user_input == "R" and computer_input == "S":
        print("you won")
        user_win += 1
        

    elif user_input == "P" and computer_input == "R":
         print("you won")
         user_win += 1
         

    elif user_input == "S" and computer_input == "P":
         print("you won")
         user_win += 1

    elif user_input == computer_input:
        print("tie")

    
    else:
        print("you lost")
        comp_win += 1
print("the user won " +str(user_win)+ " number of times")
print("the computer won " +str(comp_win)+ " number of times")
if user_win > comp_win:
    print("you are the ultimate winner")
elif user_win == comp_win:
    print('it was a tie')
else:
    print("you lost")
print('that was nice, goodbye')